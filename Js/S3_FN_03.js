const makeAdder = x => y => x + y;

const add5 = makeAdder(5);
console.log(add5(10));  // 15

const add10 = makeAdder(10);
console.log(add10(5));  // 15