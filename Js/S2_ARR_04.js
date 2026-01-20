function flatten1(arr) {
    return arr.flat();
}

console.log(flatten1([1, [2, 3], [4], 5]));  // [1, 2, 3, 4, 5]
console.log(flatten1([1, 2, [3, 4], 5]));    // [1, 2, 3, 4, 5]
console.log(flatten1([[1], [2], [3]]));       // [1, 2, 3]