function trim(str) {
    return str.trim();
}

function lowercase(str) {
    return str.toLowerCase();
}

function replaceMultipleSpaces(str) {
    return str.replace(/\s+/g, ' ');
}

function pipe(...fns) {
    return x => fns.reduce((v, f) => f(v), x);
}

const normalizeString = pipe(trim, lowercase, replaceMultipleSpaces);

console.log(normalizeString("   Hello   WORLD   "));  // "hello world"