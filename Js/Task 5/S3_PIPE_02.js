function compose(...fns) {
    return x => fns.reduceRight((v, f) => f(v), x);
}

const add = x => x + 1;
const multiply = x => x * 2;

const result = compose(multiply, add)(3);  // multiply(add(3)) = (3 + 1) * 2 = 8
console.log(result);