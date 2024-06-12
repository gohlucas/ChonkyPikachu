//Main purpose: Fetch list of buildings from API end point and display room names in dropdown menu 
import React, { useEffect, useState } from "react";
import axios from "axios";

type Building = {
  BuildingId: number;
  BuildingName: string;
};

const BuildingsList: React.FC = () => {
  const [loading, setLoading] = useState<boolean>(true); //Track if data is currently being fetched
  const [error, setError] = useState<string | null>(null); //State to store any error message if data fetching fails
  const [options, setOptions] = useState<string[]>([]); //Store list of building names

  useEffect(() => {
    const fetchBuildings = async () => {
      try {
        const response = await axios.get<Building[]>("/api/buildings"); //Fetch building data from /api.buildings, which returns the building list from database
        setOptions(response.data.map((building) => building.BuildingName)); //Update options state with the building names available
      } catch (error) { //Error handling
        console.error("Error fetching building:", error);
        setError("Error fetching building");
        console.log(error);
      } finally { //Finished
        setLoading(false);
      }
    };

    fetchBuildings();
  }, []);

  if (loading) {
    return <p>Loading...</p>; //Display loading message while data is being fetched
  }

  if (error) {
    return <p>{error}</p>; //Display error message if fetching data fails
  }
  //Function to handle changes in dropdown selection and log selected option
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
