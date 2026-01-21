function findFirstEven(nums) {
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % 2 === 0) {
            return nums[i];
        }
    }
    return null;
}

console.log(findFirstEven([1, 3, 5, 7, 8, 10]));  // 8
console.log(findFirstEven([1, 3, 5]));             // null