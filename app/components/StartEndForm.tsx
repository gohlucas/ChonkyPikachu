"use client";
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";
import "./submitbutton.css";
import { Room } from "./model";

export async function fetchRooms() {
  // Call on api to fetch response which queries database
  const response = await axios.get<Room[]>("/api/rooms");
  return response;
}

export async function fetchPath(startRoom: string, endRoom: string) {
  // Feeds user input to api to retrieve path
  const response = await fetch(
    `/api/networkx?start=${startRoom}&end=${endRoom}`
  );
  return response;
}

// Functional Component to process user input
const StartEndForm: React.FC = () => {
  const [rooms, setRooms] = useState<Room[]>([]);
  const [startRoom, setStartRoom] = useState<string>("");
  const [endRoom, setEndRoom] = useState<string>("");
  const [message, setMessage] = useState<string>("");
  const [imageList, setImageList] = useState<string[]>([]);
  const [pathList, setPathList] = useState<string[]>([]);

  const router = useRouter();

  // Push changes to localStorage upon change of variable state
  useEffect(() => {
    if (pathList.length > 0 && imageList.length > 0) {
      // Store path in localStorage
      localStorage.setItem("path", JSON.stringify(pathList));
      localStorage.setItem("image", JSON.stringify(imageList));
      console.log("This is the pathList: ", pathList);
      console.log("This is the imageList: ", imageList);
      // Navigate to the Output page
      router.push("/output");
    }
  }, [pathList, imageList]);

  // Pull list of rooms from MySQL db for users to select from
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
    if (!startRoom || !endRoom) {
      setMessage("Please select both start and end rooms.");
      return;
    }

    if (startRoom === endRoom) {
      setMessage("Please select different start and end rooms.");
      return;
    }

    try {
      // Feeds user input to api to retrieve path
      const response = await fetchPath(startRoom, endRoom);
      const data = await response.json();
      setMessage("Rooms selected successfully!");

      const path_temp = data;
      console.log("raw data for path: ", path_temp);

      // Declare variable types
      const pathDescriptionList: string[] = [];
      const urlList: string[] = [];

      // path is a list taken from networkx containing the description of path to take and the corresponding image to show user
      // ["urlforimg1", "path1", "urlforimg2", "path2"...]
      path_temp.forEach((element: string, index: number) => {
        if (index % 2 === 0) {
          urlList.push(element);
        } else {
          pathDescriptionList.push(element);
        }
      });

      console.log("This is the urlList: ", urlList);
      console.log("This is the pathDescriptionList: ", pathDescriptionList);
      console.log("break");
      // separate info into 2 lists
      setPathList(pathDescriptionList);
      setImageList(urlList);
    } catch (error) {
      console.error("Error submitting rooms:", error);
      setMessage("Error submitting rooms");
    }
  };

  return (
    // Listens for user activity and changes the room value accordingly
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
              <select
                value={endRoom}
                onChange={(e) => setEndRoom(e.target.value)}
              >
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
          {message && <p className="error-message">{message}</p>}
          <button type="submit" className="button">
            Navigate!
          </button>
        </form>
        <button className="page-link" onClick={() => router.back()}></button>
      </div>
    </div>
  );
};

export default StartEndForm;
