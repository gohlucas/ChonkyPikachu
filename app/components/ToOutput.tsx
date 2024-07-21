"use client";
import React, { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Swal from "sweetalert2";

export async function fetchPath(startRoom: string, endRoom: string) {
  // Feeds user input to api to retrieve path
  const response = await fetch(
    `/api/networkx?start=${startRoom}&end=${endRoom}`
  );
  return response;
}

const ToOutput: React.FC = () => {
  const [startRoom, setStartRoom] = useState<string>("");
  const [endRoom, setEndRoom] = useState<string>("");
  const [imageList, setImageList] = useState<string[]>([]);
  const [pathList, setPathList] = useState<string[]>([]);

  const router = useRouter();

  const process = async () => {
    if (!startRoom || !endRoom) {
      Swal.fire("Error, Start or End not valid, please try again");
      return;
    }

    if (startRoom === endRoom) {
      Swal.fire("Error, Start and End same");
      return;
    }

    try {
      console.log("this is startRoom: " + startRoom);
      console.log("this is endRoom: " + endRoom);
      // Feeds user input to api to retrieve path
      const response = await fetchPath(startRoom, endRoom);
      const data = await response.json();
      // Swal.fire("Rooms selected successfully");

      const path_temp = data;
      // console.log("raw data for path: ", path_temp);

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
      Swal.fire("Error");
    }
  };

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

  // check if the user was routed from the modTableOutput page to here
  useEffect(() => {
    const venue_start = localStorage.getItem("venue_preset_start");
    const venue_end = localStorage.getItem("venue_preset_end");
    // console.log("this is the venue as recorded in user form " + venue);
    // OVER HERE MAKE IT IF START IF END THEN IF START AND END
    if (venue_start && venue_start !== "" && venue_end && venue_end !== "") {
      // const temp_start = venue_start.length;
      // const temp = '"' + venue_start + '"';
      // console.log("this is the temp " + temp);
      setStartRoom(venue_start);
      // setStartRoom(venue_start.substring(1, temp_start - 1));

      // remove inverted commas from the string pulled from modTableOutput
      const temp_end = venue_end.length;
      // setEndRoom(venue_end);
      setEndRoom(venue_end.substring(1, temp_end - 1));

      localStorage.removeItem("venue_preset_start");
      localStorage.removeItem("venue_preset_end");
    }
    // localStorage.removeItem("venue_preset_start");
    // localStorage.removeItem("venue_preset_end");
  }, []);

  useEffect(() => {
    if (startRoom && endRoom) {
      process();
    }
  }, [startRoom, endRoom]);

  return <div> Loading in progress... </div>;
};

export default ToOutput;
