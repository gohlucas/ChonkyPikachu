// import { NextRequest, NextResponse } from "next/server";
// import { PrismaClient } from "@prisma/client";

// const prisma = new PrismaClient();

// export async function GET(req: NextRequest) {
//   console.log("made it to GET"); //State settings
//   const { searchParams } = new URL(req.url);
//   const startRoomId = searchParams.get("startRoomId");
//   const endRoomId = searchParams.get("endRoomId");

//   if (!startRoomId || !endRoomId) { //Error handling
//     return NextResponse.json(
//       { error: "Missing startRoomId or endRoomId" },
//       { status: 400 }
//     );
//   }

//   try {
//     console.log(`Fetching paths from ${startRoomId} to ${endRoomId}`);

//     const paths = await prisma.paths.findMany({
//       where: {
//         FromRoomID: parseInt(startRoomId),
//         ToRoomID: parseInt(endRoomId),
//       },
//       orderBy: {
//         PathID: 'asc',
//       },
//     });

//     console.log(`Paths found: ${paths.length}`);

//     const pathIds = paths.map(path => path.PathID);

//     const images = await prisma.pathImages.findMany({ //Find images
//       where: {
//         PathID: {
//           in: pathIds,
//         },
//       },
//     });

//     console.log(`Images found: ${images.length}`);

//     if (paths.length > 0) {
//       const response = paths.map(path => {
//         const image = images.filter(img => img.PathID === path.PathID).map(img => img.ImageURL);
//         return {
//           PathID: path.PathID,
//           instruction: path.PathDescription,
//           images: image,
//         };
//       });

//       return NextResponse.json(response);
//     } else {
//       return NextResponse.json({ message: "No paths found" }, { status: 404 });
//     }
//   } catch (error) {
//     console.error("Error querying paths and images:", error); //Error handling
//     return NextResponse.json(
//       { error: "Error querying paths and images" },
//       { status: 500 }
//     );
//   }
// }
