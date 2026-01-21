function sumNested(matrix) {
    let total = 0;
    for (let row of matrix) {
        for (let num of row) {
            total += num;
        }
    }
    return total;
}

console.log(sumNested([[1, 2], [3, 4], [5]]));  // 15
console.log(sumNested([[1, 2, 3], [4, 5], [6]]));  // 21