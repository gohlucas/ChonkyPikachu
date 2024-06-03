import React, { useEffect, useState } from "react";
import axios from "axios";

type Room = {
  BuildingId: number;
  RoomId: number;
  RoomName: string;
};

const RoomsList: React.FC = () => {
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [options, setOptions] = useState<string[]>([]);

  useEffect(() => {
    const fetchRooms = async () => {
      try {
        const response = await axios.get<Room[]>("/api/rooms");
        setOptions(response.data.map((room) => room.RoomName));
      } catch (error) {
        console.error("Error fetching rooms:", error);
        setError("Error fetching rooms");
        console.log(error);
      } finally {
        setLoading(false);
      }
    };

    fetchRooms();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  const handleSelect = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedOption = event.target.value;
    // Do something with the selected option
    console.log("Selected option:", selectedOption);
  };

  return (
    <div>
      <select onChange={handleSelect}>
        <option value="">Select...</option>
        {options.map((option, index) => (
          <option key={index} value={option}>
            {option}
          </option>
        ))}
      </select>
    </div>
  );
};

export default RoomsList;
