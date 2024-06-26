import { NextRequest, NextResponse } from "next/server";
import axios from "axios";

// Collects information from url of GET request and sends it to the
// server to get networkx to compute data and return it
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const start = searchParams.get("start");
  const end = searchParams.get("end");

  if (!start || !end) {
    return NextResponse.json(
      { error: "Please provide both start and end parameters" },
      { status: 400 }
    );
  }

  try {
    const response = await axios.get(
      `https://chonkypikachu.pythonanywhere.com/shortest_path`,
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
