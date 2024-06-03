"use client";
import React, { useState, useEffect } from "react";
import axios from "axios";

type Room = {
  BuildingID: number;
  RoomID: number;
  RoomName: string;
};

const StartEndForm: React.FC = () => {
  const [rooms, setRooms] = useState<Room[]>([]);
  const [startRoom, setStartRoom] = useState<string>("");
  const [endRoom, setEndRoom] = useState<string>("");
  const [message, setMessage] = useState<string>("");
  const [msg, setMsg] = useState<string>("");

  useEffect(() => {
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

    if (startRoom != "1") {
      setMessage("Please choose Discussion Room 1 as Start Room for testing");
      return;
    }

    try {
      const response = await axios.get("/api/paths", {
        params: {
          startRoomId: startRoom,
          endRoomId: endRoom,
        },
      });
      setMessage("Rooms selected successfully!");
      console.log(response.data);
      setMsg(response.data.PathDescription);
    } catch (error) {
      console.error("Error submitting rooms:", error);
      setMessage("Error submitting rooms");
    }
  };

  return (
    <div>
      <h1>Select Start and End Rooms</h1>
      <form onSubmit={handleSubmit}>
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
                value={room.RoomID || "-1"}
              >
                {room.RoomName}
              </option>
            ))}
          </select>
        </label>
        <br />
        <label>
          End Room:
          <select value={endRoom} onChange={(e) => setEndRoom(e.target.value)}>
            <option value="">Select...</option>
            {rooms.map((room) => (
              <option
                key={`end-${room.BuildingID}-${room.RoomID}`}
                value={room.RoomID || "-1"}
              >
                {room.RoomName}
              </option>
            ))}
          </select>
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
      {message && <p>{message}</p>}
      {msg && <p>{msg}</p>}
    </div>
  );
};

export default StartEndForm;
