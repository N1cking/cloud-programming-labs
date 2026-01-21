function omit(obj, keys) {
    const result = { ...obj };
    for (let key of keys) {
        delete result[key];
    }
    return result;
}

const obj = { a: 1, b: 2, c: 3 };
const keys = ['a', 'c'];

console.log(omit(obj, keys));  // { b: 2 }