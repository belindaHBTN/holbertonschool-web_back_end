export default function cleanSet(set, startString) {
  const result = [];
  if (startString === '') {
    return '';
  }

  for (const string of set) {
    if (string.startsWith(startString)) {
      const restOfString = string.slice(3);
      result.push(restOfString);
    }
  }

  return result.join('-');
}
