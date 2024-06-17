"use client";
import React, { useState } from "react";
import Link from "next/link";
import BuildingsList from "../components/BuildingsList";
import RoomsList from "../components/RoomsList";
import StartEndForm from "../components/StartEndForm";

const page = () => {
  return (
    <div style={{ color: "black" }}>
      <h1>ChonkyPikachu</h1>
      <br></br>
      <StartEndForm />
      <Link href="/">Back</Link>
    </div>
  );
};

export default page;
