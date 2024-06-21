import React from "react";
import StartEndForm from "../components/StartEndForm";
import './mainpage.css';

const HomePage: React.FC = () => {
  return (
    <div className="page-container">
      <h1 className="page-title">ConveNUS</h1>
      <div className="page-form">
        <StartEndForm />
      </div>
    </div>
  );
};

export default HomePage;