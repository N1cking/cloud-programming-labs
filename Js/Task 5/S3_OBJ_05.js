function invert(obj) {
    const result = {};
    for (let key in obj) {
        const value = obj[key];
        if (result[value]) {
            result[value].push(key);
        } else {
            result[value] = [key];
        }
    }
    return result;
}

const obj = { a: 1, b: 2, c: 1 };
console.log(invert(obj));  // { '1': ['a', 'c'], '2': ['b'] }