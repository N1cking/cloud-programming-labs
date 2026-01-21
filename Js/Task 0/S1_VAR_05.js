function isArray(value) {
    return Array.isArray(value);
}

console.log(isArray([1, 2, 3]));  // true
console.log(isArray({ a: 1 }));   // false
console.log(isArray("Hello"));    // false
console.log(isArray(42));         // false