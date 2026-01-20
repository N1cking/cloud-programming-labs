function pipe(...fns) {
    return x => fns.reduce((v, f) => f(v), x);
}

const add = x => x + 1;
const multiply = x => x * 2;

const result = pipe(add, multiply)(3);  // (3 + 1) * 2 = 8
console.log(result);