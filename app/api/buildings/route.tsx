import { NextRequest, NextResponse } from "next/server";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function GET(request: NextRequest) {
  try {
    const buildings = await prisma.buildings.findMany();
    console.log("from route for buildings ok");
    return NextResponse.json(buildings);
  } catch (error) {
    console.error("Error fetching buildings", error);
    console.log("error from route");
    return new NextResponse("Internal Server Error", { status: 500 });
  }
}
