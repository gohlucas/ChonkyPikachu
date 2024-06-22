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
      <header className="output-header">
        <div>Output</div>
      </header>
      <div className="output-content">
        {/* Display the navigation results or any other information here */}
        {path.length > 0 && (
          <div>
            <p>Path: {path.join(', ')}</p>
          </div>
        )}
      </div>
    </main>
  );
};

export default Output;