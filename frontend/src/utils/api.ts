export const fetchSheet = async (sheetId: string) => {
  const response = await fetch("http://127.0.0.1:8000/fetch-sheet/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sheet_id: sheetId }),
  });
  return response.json();
};

export const processSheet = async (sheetId: string) => {
  const response = await fetch("http://127.0.0.1:8000/process-sheet/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sheet_id: sheetId }),
  });
  return response.json();
};

export const downloadCSV = async () => {
  const response = await fetch("http://127.0.0.1:8000/download/");
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "processed_sheet.csv";
  a.click();
};
