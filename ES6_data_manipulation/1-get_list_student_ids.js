export default function getListStudentIds(students) {
  if (typeof students === 'object') {
    return students.map((student) => student.id);
  }
  return [];
}
