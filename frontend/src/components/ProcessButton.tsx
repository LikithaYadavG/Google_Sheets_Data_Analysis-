import React from "react";

interface Props {
  handleProcess: () => void;
}

const ProcessButton: React.FC<Props> = ({ handleProcess }) => (
  <button
    onClick={handleProcess}
    className="w-24 h-8 rounded-full  shadow-lg bg-white font-serif"
  >
    Process
  </button>
);

export default ProcessButton;
