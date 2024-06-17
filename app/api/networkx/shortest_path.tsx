import { NextRequest, NextResponse } from "next/server";

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
    const response = await fetch(
      `https://chonkypikachu.onrender.com/shortest-path?start=${start}&end=${end}`
    );
    const data = await response.json();

    if (response.ok) {
      return NextResponse.json(data, { status: 200 });
    } else {
      return NextResponse.json(data, { status: response.status });
    }
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to fetch the shortest path" },
      { status: 500 }
    );
  }
}
