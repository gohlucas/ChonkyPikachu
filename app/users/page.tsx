"use client";
import React from "react";
import StartEndForm from "../components/StartEndForm";
import "./mainpage.css"; //Styling
import { useRouter } from "next/navigation";
import "./mainpage.css"; //Styling

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
    </div>
  );
};

export default HomePage;
