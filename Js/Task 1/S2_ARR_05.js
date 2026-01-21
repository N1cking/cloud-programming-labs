function stats(nums) {
    if (nums.length === 0) return null;
    
    const min = Math.min(...nums);
    const max = Math.max(...nums);
    const avg = nums.reduce((acc, num) => acc + num, 0) / nums.length;
    
    return { min, max, avg };
}

console.log(stats([1, 2, 3, 4, 5]));   // { min: 1, max: 5, avg: 3 }
console.log(stats([10, 20, 30]));      // { min: 10, max: 30, avg: 20 }
console.log(stats([5, 10, 15, 20, 25])); // { min: 5, max: 25, avg: 15 }
console.log(stats([]));                // null