function cleanNumbers(arr) {
    return arr.map(item => +item).filter(item => !isNaN(item));
}

console.log(cleanNumbers([" 1 ", "x", "2"]));  // [1, 2]
console.log(cleanNumbers(["1", "2", " 3", "abc"]));  // [1, 2, 3]
