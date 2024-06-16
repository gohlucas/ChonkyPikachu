"use client";
import React from "react";
import Link from "next/link";
import BuildingsList from "../components/BuildingsList";
import RoomsList from "../components/RoomsList";
import StartEndForm from "../components/StartEndForm";
import './mainpage.css'; 

const Page = () => {
  return (
    <div className="page-container">
      <h1 className="page-title">ChonkyPikachu</h1>
      <div className="page-form">
        <StartEndForm />
      </div>
      <Link href="/" className="page-link">Back</Link>
    </div>
  );
};

export default Page;