function pick(obj, keys) {
    const result = {};
    for (let key of keys) {
        if (key in obj) {
            result[key] = obj[key];
        }
    }
    return result;
}

const obj = { a: 1, b: 2, c: 3 };
const keys = ['a', 'c'];

console.log(pick(obj, keys));  // { a: 1, c: 3 }