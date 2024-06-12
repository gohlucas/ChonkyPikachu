//Main purpose: Returns all records of rooms available for selection
import { NextRequest, NextResponse } from "next/server";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function GET(request: NextRequest) {
  try {
    const rooms = await prisma.rooms.findMany(); //Queries rooms table to retrieve all records
    console.log("from route ok");
    return NextResponse.json(rooms); //Returns fetched rooms records as JSON response
  } catch (error) { //Error handling
    console.error("Error fetching rooms:", error);
    console.log("error from route rooms");
    return new NextResponse("Internal Server Error", { status: 500 });
  }
}
