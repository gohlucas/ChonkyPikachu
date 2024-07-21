"use client";
import React, { useEffect, useState } from "react";
import "./styling.css";
import { timetable } from "../components/model";
import { useRouter } from "next/navigation";
import hashMap from "./venueValidator";
import Swal from "sweetalert2";

const modTableOutput: React.FC = () => {
  const [data, setData] = useState<timetable[]>([]);
  const [venue, setVenue] = useState<string>("");

  const router = useRouter();

  useEffect(() => {
    if (venue && venue.length > 0) {
      localStorage.setItem("venue_preset_end", JSON.stringify(venue));
      console.log(localStorage.getItem("venue_preset_end"));
      router.push("/loading");
    }
  }, [venue]);

  // Retrieves data from localStorage and passes it to OutputHandler
  // to display to the user
  useEffect(() => {
    const storedModData = localStorage.getItem("modData");

    if (storedModData) {
      setData(JSON.parse(storedModData));
    }
    console.log(storedModData);
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>Lesson Type</th>
          <th>Day of the Week</th>
          <th>Time Slot</th>
          <th>Mod Code</th>
          <th>Venue</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr
            key={index}
            onClick={() => {
              if (hashMap.has(item.venue)) {
                const temp = hashMap.get(item.venue);
                if (temp) {
                  setVenue(temp);
                }
              } else {
                Swal.fire("Venue not in database, please select another venue");
              }
            }}
          >
            <td>{item.lessonType}</td>
            <td>{item.day}</td>
            <td>
              {item.startTime}-{item.endTime}
            </td>
            <td>{item.classNo}</td>
            <td>{item.venue}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default modTableOutput;
