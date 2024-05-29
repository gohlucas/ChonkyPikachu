// "use client";
import React, { useState } from "react";
import DropDown from "../components/DropDown";

interface Option {
  label: string;
  value: string;
}

const page = () => {
  return (
    <div>
      <h1>ChonkyPikachu</h1>
      <h3>Which building are you currently in?</h3>
      <DropDown />
      <h3>Choose the nearest room to your desired start point</h3>
      <DropDown />
      <h3>Choose the nearest room to your desired end point</h3>
      <DropDown />
    </div>
  );
};

export default page;