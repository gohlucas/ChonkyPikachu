"use client";
import { useState, ChangeEvent } from "react";

const Dropdown = () => {
  const [selectedOption, setSelectedOption] = useState("");

  const handleDropdownChange = (event: ChangeEvent<HTMLSelectElement>) => {
    // Update event type
    setSelectedOption(event.target.value);
  };

  return (
    <div>
      <select value={selectedOption} onChange={handleDropdownChange}>
        <option value="">Select an option</option>
        <option value="option1">Room 01-21</option>
        <option value="option2">Option 01-22</option>
        <option value="option3">Option 01-23</option>
      </select>
    </div>
  );
};

export default Dropdown;
