import React, { useEffect, useState } from "react";
import axios from "axios";

type Building = {
  buildingid: number;
  level: number;
  roomname: number;
};

const BuildingData: React.FC = () => {
  const [building, setBuilding] = useState<Building[]>([]);

  useEffect(() => {
    const fetchBuildings = async () => {
      try {
        const response = await axios.get<Building[]>("/api/building");
        setBuilding(response.data);
      } catch (error) {
        console.error("Error fetching Buildings: ", error);
      }
    };
    fetchBuildings();
  }, []);

  return (
    <div>
      <h1>Building List</h1>
      <ul>
        {building.map((building) => (
          <li key={building.roomname}>
            {building.buildingid} - {building.roomname}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BuildingData;
