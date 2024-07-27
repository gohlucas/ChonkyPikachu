"use client";
import React, { useState, useEffect } from "react";
import axios from "axios";
import "./submitbutton.css";
import { Room } from "./model";
import { useRouter } from "next/navigation";

export async function fetchMods(acadYear: string, sem: string) {
  // Call on api to fetch response which queries database
  const response = await axios.get<string[]>(
    `/api/allMods?year=${acadYear}&sem=${sem}`
  );
  return response;
}

export async function fetchRooms() {
  // Call on api to fetch response which queries database
  const response = await axios.get<Room[]>("/api/rooms");
  return response;
}

export async function fetchResults(mod: string, year: string, sem: string) {
  const response = await fetch(
    `/api/nusmods?mod=${mod}&year=${year}&sem=${sem}`
  );
  return response;
}

export async function createYear(currYear: number) {
  const yearList = [];
  for (let i = currYear - 6; i <= currYear; i++) {
    yearList.push(`${i}-${i + 1}`);
  }
  return yearList;
}

// Functional Component to process user input
const ModLocation: React.FC = () => {
  const [mods, setMods] = useState<string[]>([]);
  const [chosenMod, setChosenMod] = useState<string>("");
  const [chosenSem, setChosenSem] = useState<string>("");
  const [message, setMessage] = useState<string>("");
  const [modData, setModDataList] = useState<string[]>([]);
  const [acadYear, setAcadYear] = useState<string>("");
  const [yearList, setYearList] = useState<string[]>([]);
  const [rooms, setRooms] = useState<Room[]>([]);
  const [startRoom, setStartRoom] = useState<string>("");
  const [currSem, setCurrSem] = useState<string[]>([
    "Semester 1",
    "Semester 2",
  ]);

  const router = useRouter();

  useEffect(() => {
    const fetchYearList = async () => {
      const yr: number = new Date().getFullYear();
      const temp: string[] = await createYear(yr);
      setYearList(temp);
    };
    fetchYearList();
  }, []);

  useEffect(() => {
    if (modData.length > 0) {
      // Store path in localStorage
      localStorage.setItem("modData", JSON.stringify(modData));
      // Navigate to the modTableOutput page
      router.push("/modTableOutput");
    }
  }, [modData]);

  // Pull list of modules from MySQL db for users to select from
  useEffect(() => {
    // Call on api to fetch response which queries database
    const fetchModsAsync = async () => {
      try {
        const response = await fetchMods(acadYear, chosenSem);
        console.log(response.data);
        setMods(response.data);
      } catch (error) {
        console.error("Error fetching mods:", error);
      }
    };
    if (acadYear && chosenSem) {
      fetchModsAsync();
    }
  }, [acadYear, chosenSem]);

  useEffect(() => {
    // Call on api to fetch response which queries database
    const fetchRoomsAsync = async () => {
      try {
        const response = await fetchRooms();
        setRooms(response.data);
      } catch (error) {
        console.error("Error fetching rooms:", error);
      }
    };
    fetchRoomsAsync();
  }, []);

  const handleSubmit = async (event: React.FormEvent) => {
    //Form submission
    event.preventDefault();
    if (!acadYear || !chosenMod || !startRoom || !chosenSem) {
      setMessage(
        "Please select Academic Year, Semester, Module and Start Room."
      );
      return;
    }

    try {
      localStorage.setItem("venue_preset_start", startRoom);
      // Feeds user input to api to retrieve details
      const response = await fetchResults(chosenMod, acadYear, chosenSem);
      const data = await response.json();
      if (!data || data.length === 0) {
        setMessage(
          "Please Select another Module, no venue for this Module found"
        );
      } else {
        setMessage("Locating...");
        setModDataList(data);
      }
    } catch (error) {
      console.error("Error:", error);
      setMessage("Error");
    }
  };

  return (
    // Listens for user activity and changes the room value accordingly
    <div>
      <h1>Select Module</h1>
      <h2>Please Select Academic Year and Semester before Module</h2>
      <div>
        <form onSubmit={handleSubmit}>
          <div>
            <label>
              Academic Year:
              <select
                value={acadYear}
                onChange={(e) => {
                  setAcadYear(e.target.value);
                }}
              >
                <option value="">Select...</option>
                {yearList.map((module, index) => (
                  <option key={index} value={module}>
                    {module}
                  </option>
                ))}
              </select>
            </label>
            <label>
              Semester:
              <select
                value={chosenSem}
                onChange={(e) => {
                  setChosenSem(e.target.value);
                }}
              >
                <option value="">Select...</option>
                {currSem.map((sem, index) => (
                  <option key={index} value={index}>
                    {sem}
                  </option>
                ))}
              </select>
            </label>
            <label>
              Module:
              <select
                value={chosenMod}
                onChange={(e) => {
                  setChosenMod(e.target.value);
                }}
              >
                <option value="">Select...</option>
                {mods.map((module, index) => (
                  <option key={index} value={module}>
                    {module}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <div>
            <label>
              Start Room:
              <select
                value={startRoom}
                onChange={(e) => setStartRoom(e.target.value)}
              >
                <option value="">Select...</option>
                {rooms.map((room) => (
                  <option
                    key={`start-${room.BuildingID}-${room.RoomID}`}
                    value={room.RoomNumber}
                  >
                    {room.RoomName}
                  </option>
                ))}
              </select>
            </label>
          </div>
          {message && <p className="error-message">{message}</p>}
          <button type="submit">Find your venue!</button>
        </form>
        <div>
          * Due to limitations in mapping of buildings due to time constraint,
          please only choose modules with lessons in COM1
        </div>
        <div>for example: CS1010, CS1231, CS2040</div>
      </div>
    </div>
  );
};

export default ModLocation;
