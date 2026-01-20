function get(obj, path, fallback) {
    const keys = path.split('.');
    let result = obj;
    for (let key of keys) {
        if (result && key in result) {
            result = result[key];
        } else {
            return fallback;
        }
    }
    return result;
}

const obj = { a: { b: { c: 42 } } };

console.log(get(obj, "a.b.c", "Not found"));  // 42
console.log(get(obj, "a.b.d", "Not found"));  // "Not found"