"use client";
import React, { useState, useEffect } from "react";
import axios from "axios";

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
  const [length, setLength] = useState(null);
  const [path, setPath] = useState([]);

  useEffect(() => {
    setLength(null);
    setPath([]);
    const fetchRooms = async () => {
      try {
        // get list of all rooms documented for the user to choose from
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
    // input handling from user end
    if (!startRoom || !endRoom) {
      setMessage("Please select both start and end rooms.");
      return;
    }

    if (startRoom === endRoom) {
      setMessage("Please select different start and end rooms.");
      return;
    }

    try {
      // const response = await axios.get<PathDetail[]>("/api/paths", {
      //send user's start and end room to flask so that networkx can compute the shortest path
      const response = await axios.get("/api/shortest_path", {
        params: {
          start: startRoom,
          end: endRoom,
        },
      });
      // console.log(response.data); // Log the response to verify images are included
      setMessage("Rooms selected successfully!");
      // setPathDetails(response.data);
      // example of the json response for instructions
      // {
      //   "length": 1,
      //   "path": [
      //     "1",
      //     "2"
      //   ]
      // }
      // store the response as variables
      const { length, path } = response.data;
      setLength(length);
      setPath(path);
      setTemp(path + " " + length);
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
                value={room.RoomNumber}
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
                value={room.RoomNumber}
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
    </div>
  );
};

export default StartEndForm;
