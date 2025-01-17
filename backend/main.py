from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse
import gspread
from statistics import mean, median, mode
import csv
import os

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SheetID(BaseModel):
    sheet_id: str

# Authenticate with Google Sheets using service account credentials
gc = gspread.service_account(filename="credentials.json")

def calculate_metrics(sheet):
    data = sheet.get_all_values()
    header, *rows = data

    # Transpose rows to columns for easier processing
    columns = list(zip(*rows))

    metrics = {
        "Total": [],
        "Average": [],
        "Median": [],
        "Mode": [],
    }

    for column in columns:
        # Convert column to numeric values where possible
        numeric_column = [
            float(value) for value in column if value.replace(".", "", 1).isdigit()
        ]

        if numeric_column:
            metrics["Total"].append(sum(numeric_column))
            metrics["Average"].append(mean(numeric_column))
            metrics["Median"].append(median(numeric_column))
            try:
                metrics["Mode"].append(mode(numeric_column))
            except:
                metrics["Mode"].append("No unique mode")
        else:
            metrics["Total"].append("N/A")
            metrics["Average"].append("N/A")
            metrics["Median"].append("N/A")
            metrics["Mode"].append("N/A")

    return metrics

@app.post("/fetch-sheet/")
async def fetch_sheet(sheet_id: SheetID):
    try:
        sheet = gc.open_by_key(sheet_id.sheet_id).sheet1
        data = sheet.get_all_values()  # Fetch all rows including headers
        return {"message": "Sheet fetched successfully", "data": data}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error fetching sheet: {str(e)}")


@app.post("/process-sheet/")
async def process_sheet(sheet_id: SheetID):
    try:
        sheet = gc.open_by_key(sheet_id.sheet_id).sheet1

        # Calculate metrics
        metrics = calculate_metrics(sheet)

        # Append metrics to the sheet
        sheet.append_row(["Total"] + metrics["Total"], value_input_option="USER_ENTERED")
        sheet.append_row(["Average"] + metrics["Average"], value_input_option="USER_ENTERED")
        sheet.append_row(["Median"] + metrics["Median"], value_input_option="USER_ENTERED")
        sheet.append_row(["Mode"] + metrics["Mode"], value_input_option="USER_ENTERED")

        # Fetch updated data and save as a CSV
        data = sheet.get_all_values()
        file_path = "processed_sheet.csv"
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        return {"message": "Sheet processed and CSV saved"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing sheet: {str(e)}")




@app.get("/download/")
async def download_csv():
    file_path = "processed_sheet.csv"
    if os.path.exists(file_path):
        return FileResponse(file_path, filename="processed_sheet.csv")
    raise HTTPException(status_code=404, detail="File not found")