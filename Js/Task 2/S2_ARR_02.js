function unique(values) {
    return values.filter((value, index, self) => self.indexOf(value) === index);
}

console.log(unique([1, 2, 3, 1, 2, 4]));  // [1, 2, 3, 4]
console.log(unique(["a", "b", "a", "c"]));  // ["a", "b", "c"]