"use client";
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useRouter } from 'next/navigation'; // Use 'next/navigation' for App Router
import "./submitbutton.css";

type Room = {
  BuildingID: number;
  RoomID: number;
  RoomName: string;
  RoomNumber: string;
};

type PathDetail = {
  PathID: number;
  instruction: string | null;
  images: string[];
};

const StartEndForm: React.FC = () => {
  const [rooms, setRooms] = useState<Room[]>([]);
  const [startRoom, setStartRoom] = useState<string>("");
  const [endRoom, setEndRoom] = useState<string>("");
  const [message, setMessage] = useState<string>("");
  const [temp, setTemp] = useState<string>("");
  const [pathDetails, setPathDetails] = useState<PathDetail[]>([]);
  const [length, setLength] = useState<number | null>(null);
  const [path, setPath] = useState<string[]>([]);
  const router = useRouter();

  useEffect(() => {
    setLength(null);
    setPath([]);
    const fetchRooms = async () => {
      try {
        const response = await axios.get<Room[]>("/api/rooms");
        setRooms(response.data);
      } catch (error) {
        console.error("Error fetching rooms:", error);
      }
    };

    fetchRooms();
  }, []);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (!startRoom || !endRoom) {
      setMessage("Please select both start and end rooms.");
      return;
    }

    if (startRoom === endRoom) {
      setMessage("Please select different start and end rooms.");
      return;
    }

    try {
      const response = await fetch(`/api/networkx?start=${startRoom}&end=${endRoom}`);
      const data = await response.json();
      setMessage("Rooms selected successfully!");
      const { length, path } = data;
      setLength(length);
      setPath(path);
      setTemp(path + " " + length);

      // Navigate to the Output page
      router.push('/output');

    } catch (error) {
      console.error("Error submitting rooms:", error);
      setMessage("Error submitting rooms");
    }
  };

  return (
    <div className="center-container">
      <h1>Select Start and End Rooms</h1>
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <div className="label-container">
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
          <div className="label-container">
            <label>
              End Room:
              <select value={endRoom} onChange={(e) => setEndRoom(e.target.value)}>
                <option value="">Select...</option>
                {rooms.map((room) => (
                  <option
                    key={`end-${room.BuildingID}-${room.RoomID}`}
                    value={room.RoomNumber}
                  >
                    {room.RoomName}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <button type="submit" className="button">Navigate!</button>
        </form>
        {message && <p>{message}</p>}
        {temp && <p>{temp}</p>}
        {pathDetails.length > 0 && (
          <div>
            {pathDetails.map((detail) => (
              <div key={detail.PathID}>
                <h2>Step {detail.PathID}</h2>
                <p>{detail.instruction}</p>
                {detail.images.length > 0 && (
                  <div>
                    {detail.images.map((url, index) => (
                      <img
                        key={index}
                        src={url}
                        alt={`Step ${detail.PathID} Image ${index + 1}`}
                      />
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
        <button className="page-link" onClick={() => router.back()}></button> {/* Add Back Button */}
      </div>
    </div>
  );
};

export default StartEndForm;