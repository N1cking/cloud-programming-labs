function classifyNumberLike(x) {
    if (Number.isNaN(x)) {
        return "nan";
    }
    if (typeof x === "number") {
        return "number";
    }
    return "not-a-number";
}

console.log(classifyNumberLike(NaN));        // "nan"
console.log(classifyNumberLike(42));         // "number"
console.log(classifyNumberLike("42"));       // "not-a-number"
console.log(classifyNumberLike("abc"));      // "not-a-number"
console.log(classifyNumberLike(undefined));  // "not-a-number"