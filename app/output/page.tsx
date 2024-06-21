import React from 'react';
import './output.css';

const Output: React.FC = () => {
  return (
    <main className="output-main">
      <header className="output-header">
        <div>Output</div>
      </header>
      <div className="output-content">
        {/* Display the navigation results or any other information here */}
      </div>
    </main>
  );
};

export default Output;