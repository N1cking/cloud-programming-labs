function mapValues(obj, fn) {
    const result = {};
    for (let key in obj) {
        result[key] = fn(obj[key]);
    }
    return result;
}

const obj = { a: 1, b: 2, c: 3 };

const newObj = mapValues(obj, val => val * 2);

console.log(newObj);  // { a: 2, b: 4, c: 6 }