"use client"
import React, { useEffect, useState } from 'react';
import './output.css';

const Output: React.FC = () => {
  const [path, setPath] = useState<string[]>([]);

  useEffect(() => {
    const storedPath = localStorage.getItem('path');

    if (storedPath) {
      setPath(JSON.parse(storedPath));
    }
  }, []);

  return (
    <main className="output-main">
      <div className="output-content-step">
        {/* Display the navigation results or any other information here */}
        {path.length > 0 && (
          <div className="output-content-step">
            <p>Path: {path.join(', ')}</p>
          </div>
        )}
      </div>
    </main>
  );
};

export default Output;