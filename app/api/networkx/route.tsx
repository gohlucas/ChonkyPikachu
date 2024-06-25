import { NextRequest, NextResponse } from "next/server";
import axios from "axios";

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const start = searchParams.get("start");
  const end = searchParams.get("end");

  console.log(`Incoming request with start=${start} and end=${end}`);

  if (!start || !end) {
    return NextResponse.json(
      { error: "Please provide both start and end parameters" },
      { status: 400 }
    );
  }

  try {
    const response = await axios.get(
      `https://chonkypikachu.pythonanywhere.com/shortest_path`,
      // `https://chonkypikachu.onrender.com/shortest_path`,
      {
        params: { start, end },
      }
    );
    return NextResponse.json(response.data, { status: 200 });
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to fetch the shortest path" },
      { status: 500 }
    );
  }
}
