"use client";
import React from "react";
import Link from "next/link";
import StartEndForm from "../components/StartEndForm";

const Page = () => {
  return (
    <div style={{ color: "black" }}>
      <h1>ChonkyPikachu</h1>
      <br></br>
      <StartEndForm />
      <Link href="/">Back</Link>
    </div>
  );
};

export default Page;
