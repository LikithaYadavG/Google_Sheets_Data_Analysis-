# Google Sheets Data Analysis Tool

This project is a Google Sheets Data Analysis tool that allows users to fetch data from a Google Sheet, perform statistical analysis (e.g., total, average, median, mode) on numeric columns, and download the processed data as a CSV file.

---

## Features

1. **Fetch Data**: Fetch data from a Google Sheet using its Sheet ID.
2. **Process Data**: Perform calculations like Total, Average, Median, and Mode for numeric columns.
3. **Download CSV**: Download the updated Google Sheet as a CSV file.
4. **Real-Time Updates**: Results are appended directly to the Google Sheet and saved locally.

---

## Requirements

### Frontend

- **Framework**: React with TypeScript
- **Styling**: Tailwind CSS
- **Packages**: `react`, `typescript`

### Backend

- **Framework**: FastAPI
- **Libraries**:
  - `gspread`: For Google Sheets API integration.
  - `statistics`: For calculating metrics (mean, median, mode).
  - `csv` and `os`: For file operations.
  - `pydantic`: For request validation.
  - `fastapi.middleware.cors`: For handling cross-origin requests.

### Other Requirements

- **Google Service Account**: Requires a `credentials.json` file to authenticate with Google Sheets API.
- **Python**: Version 3.8 or higher.
- **Node.js**: Version 14+ for running React.

---

## Installation

### 1. Clone the Repository

````bash
git clone https://github.com/LikithaYadavG/Google_Sheets_Data_Analysis-.git
cd <project-directory>
````

2. Install Dependencies
Frontend

```bash
cd frontend
npm install
````

Backend

```bash
cd backend
pip install -r requirements.txt
````


3. Setup Google Service Account
Go to Google Cloud Console.
Enable the Google Sheets API and create a service account.
Download the credentials.json file and place it in the backend directory.


Usage

Start the Backend

```bash
cd backend
uvicorn main:app --reload
````

Start the Frontend

```bash
cd frontend
npm start
````

The application will run locally on http://localhost:3000.

# Frontend Features

## File Structure

```bash

frontend/
├── components/
│   ├── SheetInput.tsx         # Input field for entering Google Sheet ID
│   ├── ProcessButton.tsx      # Button for processing data
├── utils/
│   └── api.ts                 # API functions to interact with the backend
├── App.tsx                    # Main application file
````


## Workflow
1. Enter the Google Sheet ID in the input box.  
2. Click **Fetch Sheet** to retrieve data from the Google Sheet.  
3. Click **Process** to calculate metrics and append them to the sheet.  
4. Click **Download CSV** to download the processed sheet.


Backend Features
File Structure
```bash
backend/
├── main.py                    # FastAPI backend logic
├── credentials.json           # Google service account credentials
├── processed_sheet.csv        # Output file (generated after processing)
````

## Endpoints

### POST /fetch-sheet/

  Fetches data from a Google Sheet.

  Input: { "sheet_id": "<Google Sheet ID>" }
  
  Output: Data from the sheet.
  
### POST /process-sheet/

  Performs calculations and appends results to the sheet.
  
  Input: { "sheet_id": "<Google Sheet ID>" }
  
  Output: Confirmation message and updated sheet data.
  
### GET /download/

  Provides the processed sheet as a CSV file.

## Metrics Calculated

-Total: Sum of numeric values in each column.

-Average: Mean of numeric values in each column.

-Median: Middle value of numeric values in each column.

-Mode: Most frequently occurring value in each column.


