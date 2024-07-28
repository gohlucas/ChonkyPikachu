"use client";
import React, { useEffect, useState } from "react";
import OutputHandler from "../components/OutputHandler";
import "./output.css";

const Output: React.FC = () => {
  const [path, setPath] = useState<string[]>([]);
  const [img, setImg] = useState<string[]>([]);

  // Retrieves data from localStorage and passes it to OutputHandler
  // to display to the user
  useEffect(() => {
    const storedPath = localStorage.getItem("path");
    const storedImagePath = localStorage.getItem("image");

    if (storedPath && storedImagePath) {
      setPath(JSON.parse(storedPath));
      setImg(JSON.parse(storedImagePath));
    }
    console.log("success at page output");
  }, []);

  return (
    <main className="output-main">
      <div className="output-content-step">
        <div className="output-content-step">
          <OutputHandler imageUrls={img} description={path} />
        </div>
      </div>
    </main>
  );
};

export default Output;
