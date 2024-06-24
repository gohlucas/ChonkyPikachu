"use client";
import React, { useState, useEffect } from "react";
import axios from "axios"; //Make API request
import { useRouter } from 'next/navigation'; 
import "./submitbutton.css"; //For styling

//Structure for Room and PathDetail
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
  const [rooms, setRooms] = useState<Room[]>([]); //Holds list of rooms fetched. Inital state is just empty room variable
  const [startRoom, setStartRoom] = useState<string>("");  //Stores selected start and end room
  const [endRoom, setEndRoom] = useState<string>("");
  const [message, setMessage] = useState<string>(""); //Feedback to user
  const [pathDetails, setPathDetails] = useState<PathDetail[]>([]); //Holds detail of path
  const [path, setPath] = useState<string[]>([]);  //Holds path data from API
  const router = useRouter();

  useEffect(() => {
    const fetchRooms = async () => {
      try {
        const response = await axios.get<Room[]>("/api/rooms"); //HTTP GET Request, Fetch response from /api/rooms which queries database
        setRooms(response.data);  //Sets room 
      } catch (error) {
        console.error("Error fetching rooms:", error);
      }
    };

    fetchRooms(); //Actual call
  }, []);

  const handleSubmit = async (event: React.FormEvent) => {  //Form submission
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
      const response = await fetch(`/api/networkx?start=${startRoom}&end=${endRoom}`); //Runs Networkx
      const data = await response.json();
      setMessage("Rooms selected successfully!");
      const { path } = data;
      setPath(path); 

      // Store path in localStorage
      localStorage.setItem('path', JSON.stringify(path)); //Stores path in local stroage to be used in output later 

      // Navigate to the Output page
      router.push('/output');

    } catch (error) {
      console.error("Error submitting rooms:", error);
      setMessage("Error submitting rooms");
    }
  };

  return (  //Structure of the page 
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
          {message && <p className="error-message">{message}</p>}
          <button type="submit" className="button">Navigate!</button>
        </form>
        {pathDetails.length > 0 && (
          <div>
            {pathDetails.map((detail) => (  //Iterate items in array
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
        <button className="page-link" onClick={() => router.back()}></button>  
      </div>
    </div>
  );
};

export default StartEndForm;