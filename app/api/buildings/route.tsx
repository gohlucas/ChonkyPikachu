//Main Purpoose: Fetches records from buildings table
import { NextRequest, NextResponse } from "next/server";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function GET(request: NextRequest) {
  try {
    const buildings = await prisma.buildings.findMany(); //Performs a query to fetch all records from buildings table
    console.log("from route for buildings ok");
    return NextResponse.json(buildings);  //Returns fetched buildings records as a JSON response
  } catch (error) { //Error handling
    console.error("Error fetching buildings", error);
    console.log("error from route");
    return new NextResponse("Internal Server Error", { status: 500 });
  }
}
