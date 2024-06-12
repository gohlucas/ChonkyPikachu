//Main purpose: Get from and to room and return the matching file in database
import { NextRequest, NextResponse } from "next/server";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function GET(req: NextRequest) {
  console.log("made it to GET");
  const { searchParams } = new URL(req.url); //Creates a URL object from request URL
  const startRoomId = searchParams.get("startRoomId"); //Extract query parameters from URL 
  const endRoomId = searchParams.get("endRoomId"); //Extract query parameters from URL 

  //Check if start and end room is missing 
  if (!startRoomId || !endRoomId) {
    return NextResponse.json(
      { error: "Missing startRoomId or endRoomId" },
      { status: 400 }
    );
  }

  try {
    // Queries the paths table for teh first record matching the FromRoomId and ToRoomID criteria
    const path = await prisma.paths.findFirst({
      where: {
        FromRoomID: parseInt(startRoomId), //Asssigning what user input to the varibales 
        ToRoomID: parseInt(endRoomId),
      },
    });

    if (path) {
      return NextResponse.json(path); //Path found, return as JSON response
    } else {
      return NextResponse.json({ message: "No paths found" }, { status: 404 }); //No path found
    }
  } catch (error) { //Error handling 
    console.error("Error querying paths:", error);
    return NextResponse.json(
      { error: "Error querying paths" },
      { status: 500 }
    );
  }
}
