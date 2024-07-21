"use client";
import React from "react";
import StartEndForm from "../components/StartEndForm";
<<<<<<< HEAD
import "./mainpage.css"; //Styling
=======
import { useRouter } from "next/navigation"; 
import './mainpage.css'; //Styling
>>>>>>> e4b822f7b12e0ac35b8fea5e4549f5c31751f6aa

const HomePage: React.FC = () => {
  const router = useRouter();

  const handleModelPageNavigation = () => {
    router.push("/3DModelPage");
  };

  return (
    <div className="page-container">
      <div className="page-form">
        <StartEndForm />
      </div>
      <button onClick={handleModelPageNavigation} className="button">
        View 3D Model
      </button>
    </div>
  );
};

export default HomePage;
