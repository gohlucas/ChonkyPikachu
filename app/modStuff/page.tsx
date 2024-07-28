"use client";
import React from "react";
import ModLocation from "../components/ModLocation";

//Functional component on homepage to bring users to the next page
const Home: React.FC = () => {
  const handleRefresh = () => {
    window.location.href = "/intro";
  };

  return (
    <main>
      <header>
        <div>
          <ModLocation />
          <button onClick={handleRefresh}>
            Click here to head back to Start Page
          </button>
        </div>
      </header>
    </main>
  );
};

export default Home;
