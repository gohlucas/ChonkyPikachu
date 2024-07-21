import { NextRequest, NextResponse } from "next/server";
import axios from "axios";

// Collects information from url of GET request and sends it to the
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const modName = searchParams.get("mod");
  const acadYear = searchParams.get("year");
  const sem = searchParams.get("sem");

  let semNum: number;
  if (sem == "0") {
    semNum = 0;
  } else {
    semNum = 1;
  }

  if (!modName || !acadYear) {
    return NextResponse.json(
      { error: "Please provide both start and end parameters" },
      { status: 400 }
    );
  }

  type rawData = {
    semesterData: semesterData[];
  };

  type attrib = {
    day: string;
    startTime: string;
    lessonType: string;
    classNo: string;
  };

  type semesterData = {
    timetable: attrib[];
  };

  try {
    const response = await axios.get(
      `https://api.nusmods.com/v2/${acadYear}/modules/${modName}.json`
    );
    const data: rawData = response.data;
    const transformedData: attrib[] = data.semesterData[semNum].timetable;
    if (!transformedData) {
      return NextResponse.json({}, { status: 204 });
    }
    const dayComparer = [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
    ];
    // sort by day, then if same day sort by time,
    // then if same time sort by lesson type, then if same lesson type sort by class code
    const sortedData = transformedData.sort((a, b) => {
      const dayComparator =
        dayComparer.indexOf(a.day) - dayComparer.indexOf(b.day);
      if (dayComparator !== 0) {
        return dayComparator;
      }

      const timeComparator = a.startTime.localeCompare(b.startTime);
      if (timeComparator !== 0) {
        return timeComparator;
      }

      const typeComparator = a.lessonType.localeCompare(b.lessonType);
      if (typeComparator !== 0) {
        return typeComparator;
      }

      return a.classNo.localeCompare(b.classNo);
    });
    return NextResponse.json(sortedData, { status: 200 });
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to fetch module data" },
      { status: 500 }
    );
  }
}
