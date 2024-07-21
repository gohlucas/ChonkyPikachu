// Declaration of variable types
export type Room = {
  RoomID: number;
  BuildingID: number;
  Floor: string;
  RoomNumber: string;
  RoomName: string;
};

export type Module = {
  Mod_ID: number;
  Mod_Name: String;
};

export type genericLocation = {
  Day: string;
  Time: string;
  Name: string;
  Venue: string;
  Room_Name: string;
};

export type timetable = {
  day: string;
  classNo: string;
  startTime: string;
  endTime: string;
  venue: string;
  lessonType: string;
};
