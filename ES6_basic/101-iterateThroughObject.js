export default function iterateThroughObject(reportWithIterator) {
  let string = '';

  for (let i = 0; i < reportWithIterator.length; i += 1) {
    if (i < reportWithIterator.length - 1) {
      string = `${string} ${reportWithIterator[i]} | `;
    } else {
      string = `${string} ${reportWithIterator[i]}`;
    }
  }

  return string;
}
