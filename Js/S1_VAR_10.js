function inspect(value) {
    return {
        type: typeof value,
        isArray: Array.isArray(value),
        isNull: value === null,
        isNaN: Number.isNaN(value),
    };
}

console.log(inspect(null));              // { type: "object", isArray: false, isNull: true, isNaN: false }
console.log(inspect([]));                // { type: "object", isArray: true, isNull: false, isNaN: false }
console.log(inspect(42));                // { type: "number", isArray: false, isNull: false, isNaN: false }
console.log(inspect("42"));              // { type: "string", isArray: false, isNull: false, isNaN: false }
console.log(inspect(NaN));               // { type: "number", isArray: false, isNull: false, isNaN: true }
console.log(inspect(undefined));         // { type: "undefined", isArray: false, isNull: false, isNaN: false }