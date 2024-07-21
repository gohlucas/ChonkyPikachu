import { NextRequest, NextResponse } from "next/server";
import axios from "axios";

// Extracts year from url of GET request and sends it to nusmods query
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const acadYear = searchParams.get("year");
  const sem = searchParams.get("sem");

  let semNum: number;
  if (sem == "0") {
    semNum = 0;
  } else {
    semNum = 1;
  }

  if (!acadYear || !sem) {
    return NextResponse.json(
      { error: "Error, Academic Year or Semester input invalid" },
      { status: 400 }
    );
  }

  type semesterData = {
    semester: number;
    examDuration: string;
  };

  type modList = {
    moduleCode: string;
    faculty: string;
    semesterData: semesterData[];
    // can put the module title also
    // title: string;
  };

  try {
    const response = await axios.get(
      `https://api.nusmods.com/v2/${acadYear}/moduleInfo.json`
    );
    const data: modList[] = response.data;
    // get the name only, don't need the other details
    const transformedData = data
      // get computing mods only
      .filter((item) => item.faculty == "Computing")
      // remove all mods which are not available in chosen sem by user
      .filter(
        (mod) =>
          mod.semesterData[semNum] &&
          mod.semesterData[semNum].semester === semNum + 1
      )
      .map((item) => item.moduleCode);
    return NextResponse.json(transformedData, { status: 200 });
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to fetch the shortest path" },
      { status: 500 }
    );
  }
}
