function filterInvalidNumbers(arr) {
    return arr.filter(item => !isNaN(item));
}

function convertToNumber(arr) {
    return arr.map(item => +item);
}

function doubleNumbers(arr) {
    return arr.map(item => item * 2);
}

function sum(arr) {
    return arr.reduce((total, num) => total + num, 0);
}

function pipe(...fns) {
    return x => fns.reduce((v, f) => f(v), x);
}

const processArray = pipe(filterInvalidNumbers, convertToNumber, doubleNumbers, sum);

console.log(processArray([" 1 ", "2", "3", "x", " 4 "]));  // 20