// Returns all records of rooms available for selection
import { NextRequest, NextResponse } from "next/server";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function GET(request: NextRequest) {
  try {
    // Queries rooms table to retrieve all records
    const rooms = await prisma.rooms.findMany();
    console.log("from route ok");
    return NextResponse.json(rooms);
  } catch (error) {
    console.error("Error fetching rooms:", error);
    console.log("error from route rooms");
    return new NextResponse("Internal Server Error", { status: 500 });
  }
}
