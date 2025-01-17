import React, { useState } from "react";
import SheetInput from "./components/SheetInput";
import ProcessButton from "./components/ProcessButton";
import { fetchSheet, processSheet, downloadCSV } from "./utils/api";

const App: React.FC = () => {
  const [sheetId, setSheetId] = useState<string>("");

  const handleFetch = async () => {
    const response = await fetchSheet(sheetId);
    alert(response.message);
  };

  const handleProcess = async () => {
    const response = await processSheet(sheetId);
    alert(response.message);
  };

  const handleDownload = async () => {
    await downloadCSV();
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2">
      <div className="flex flex-col items-center justify-center h-96 w-[500px] rounded-2xl bg-[#83CCD2] shadow-lg">
        <h1 className="text-2xl font-bold text-center mb-4 font-serif ">
          Google Sheets Data Analysis
        </h1>
        <SheetInput sheetId={sheetId} setSheetId={setSheetId} />
        <div className="flex flex-row items-center justify-center gap-6 mt-4">
          <button
            onClick={handleFetch}
            className="w-24 h-8 rounded-full bg-white font-serif "
          >
            Fetch Sheet
          </button>
          <ProcessButton handleProcess={handleProcess} />
          <button
            onClick={handleDownload}
            className="w-32 h-8 rounded-full bg-white font-serif "
          >
            Download CSV
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
