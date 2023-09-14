import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const roomArr = [];

  roomArr.push(new ClassRoom(19));
  roomArr.push(new ClassRoom(20));
  roomArr.push(new ClassRoom(34));

  return roomArr;
}
