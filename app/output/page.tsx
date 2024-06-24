"use client"
import React, { useEffect, useState } from 'react';
import './output.css'; //Styling

const Output: React.FC = () => {
  const [path, setPath] = useState<string[]>([]);  //Holds path data retrieved from local storage. Inital state is an empty string array

  useEffect(() => {
    const storedPath = localStorage.getItem('path'); //Retrieve path from local storage

    if (storedPath) {
      setPath(JSON.parse(storedPath));  //Parse into a Javascript array
    }
  }, []);

  return (
    <main className="output-main">
      <div className="output-content-step">
        {path.length > 0 && (  //Only displayed if there is indeed an element
          <div className="output-content-step"> 
            <p>Path: {path.join(', ')}</p> 
          </div>  //Join array elements
        )}
      </div>
    </main>
  );
};

export default Output;