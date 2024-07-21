import { fetchRooms, fetchPath } from "../components/StartEndForm";
// import { OutputHandler } from "../components/OutputHandler";
import axios from 'axios';
import { Room } from "../components/model";
import { createYear } from "../components/ModLocation";

jest.mock('axios');
const axiosMock = axios as jest.Mocked<typeof axios>;

const roomFetch: Room[] = [
    {
      "RoomID": 66,
      "BuildingID": 1,
      "Floor": "Level 2",
      "RoomNumber": "02-13",
      "RoomName": "VC Room"
    }
  ];
  
  // checks if api call via fetchRooms() returns the data in correct format
  // following the same processes in the actual file
  // also checks if correct api route is called
  describe('fetchRooms', () => {
    it('should reflect the rooms accurately', async () => {
        axiosMock.get.mockResolvedValue({ data: roomFetch });
        const result = await fetchRooms();
        expect(result.data).toStrictEqual(roomFetch);
        expect(axiosMock.get).toHaveBeenCalledWith("/api/rooms");
    });
  });

  const pathFetch: string[] = ["https://i.imghippo.com/files/JXs851719414208.png","Walk til you see the corridor on the next page",
  "https://i.imghippo.com/files/GaSET1719228399.jpg","Head straight","https://i.imghippo.com/files/KLbao1719228106.jpg","Head straight",
  "https://i.imghippo.com/files/OvufT1719495087.jpg","Your destination is along this corridor"];

  // checks if api call via fetchPath(startRoom, endRoom) returns data in correct format 
  // following the same processes in the actual file
  // also checks if correct api route is called
  describe('fetchPath', () => {
    it('should show the path information accurately', async () => {
        const mockResponse = {
            json: jest.fn().mockResolvedValue({ path: pathFetch }),
          };
        
        global.fetch = jest.fn().mockResolvedValue(mockResponse);

        const startRoom: string = "B-12-2";
        const endRoom: string = "B-03";

        const response = await fetchPath(startRoom, endRoom);
        const data = await response.json();
        // uses data.path here but in actual code there is intermediary
        // step to split data into 2 string arrays for usage
        expect(data.path).toStrictEqual(pathFetch);
        expect(global.fetch).toHaveBeenCalledWith("/api/networkx?start=B-12-2&end=B-03");
    })
  })
