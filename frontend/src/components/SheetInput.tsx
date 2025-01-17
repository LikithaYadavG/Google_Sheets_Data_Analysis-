import React from "react";

interface Props {
  sheetId: string;
  setSheetId: (value: string) => void;
}

const SheetInput: React.FC<Props> = ({ sheetId, setSheetId }) => (
  <div className="sheet-input ">
    <input
      type="text"
      value={sheetId}
      onChange={(e) => setSheetId(e.target.value)}
      placeholder="Enter Google Sheet ID "
      className="input  shadow-lg rounded-full h-8 w-96 text-center font-serif "
    />
  </div>
);

export default SheetInput;
