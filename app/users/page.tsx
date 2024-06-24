import React from "react";
import StartEndForm from "../components/StartEndForm";
import './mainpage.css'; //Styling

const HomePage: React.FC = () => {
  return (
    <div className="page-container">
      <div className="page-form"> 
        <StartEndForm />
      </div>
    </div> //Relies on StartEndForm componenet for styling and layout
  );
};

export default HomePage;