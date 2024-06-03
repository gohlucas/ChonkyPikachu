import { NextRequest, NextResponse } from "next/server";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function GET(req: NextRequest) {
  console.log("made it to GET");
  const { searchParams } = new URL(req.url);
  const startRoomId = searchParams.get("startRoomId");
  const endRoomId = searchParams.get("endRoomId");

  if (!startRoomId || !endRoomId) {
    return NextResponse.json(
      { error: "Missing startRoomId or endRoomId" },
      { status: 400 }
    );
  }

  try {
    const path = await prisma.paths.findFirst({
      where: {
        FromRoomID: parseInt(startRoomId),
        ToRoomID: parseInt(endRoomId),
      },
    });

    if (path) {
      return NextResponse.json(path);
    } else {
      return NextResponse.json({ message: "No paths found" }, { status: 404 });
    }
  } catch (error) {
    console.error("Error querying paths:", error);
    return NextResponse.json(
      { error: "Error querying paths" },
      { status: 500 }
    );
  }
}
