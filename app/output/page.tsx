"use client";
import React, { useEffect, useState } from "react";
import OutputHandler from "../components/OutputHandler";
import "./output.css";

const Output: React.FC = () => {
  const [path, setPath] = useState<string[]>([]);
  const [img, setImg] = useState<string[]>([]);

  useEffect(() => {
    const storedPath = localStorage.getItem("path");
    const storedImagePath = localStorage.getItem("image");

    if (storedPath && storedImagePath) {
      setPath(JSON.parse(storedPath));
      setImg(JSON.parse(storedImagePath));
    }
    console.log("success");
  }, []);

  return (
    <main className="output-main">
      <div className="output-content-step">
        {/* Display the navigation results or any other information here */}
        <div className="output-content-step">
          <OutputHandler imageUrls={img} description={path} />
          {/* <p>Path: {path.join(", ")}</p> */}
        </div>
      </div>
    </main>
  );
};

export default Output;
