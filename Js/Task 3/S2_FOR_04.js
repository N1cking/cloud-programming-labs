function countOccurrences(values) {
    const count = {};
    for (let value of values) {
        count[value] = (count[value] || 0) + 1;
    }
    return count;
}

console.log(countOccurrences([1, 2, 2, 3, 3, 3, 4]));  // {1: 1, 2: 2, 3: 3, 4: 1}
console.log(countOccurrences(["a", "b", "b", "a", "c"])); // {a: 2, b: 2, c: 1}