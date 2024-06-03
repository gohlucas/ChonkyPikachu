import React, { useEffect, useState } from "react";
import axios from "axios";

type Building = {
  BuildingId: number;
  BuildingName: string;
};

const BuildingsList: React.FC = () => {
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [options, setOptions] = useState<string[]>([]);

  useEffect(() => {
    const fetchBuildings = async () => {
      try {
        const response = await axios.get<Building[]>("/api/buildings");
        setOptions(response.data.map((building) => building.BuildingName));
      } catch (error) {
        console.error("Error fetching building:", error);
        setError("Error fetching building");
        console.log(error);
      } finally {
        setLoading(false);
      }
    };

    fetchBuildings();
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

export default BuildingsList;
