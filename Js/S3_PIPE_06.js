function pipeSafe(...fns) {
    return x => {
        try {
            let result = x;
            for (let fn of fns) {
                result = fn(result);
            }
            return { ok: true, value: result };
        } catch (error) {
            return { ok: false, error: error.message };
        }
    };
}

function add(x) {
    return x + 1;
}

function divide(x) {
    if (x === 0) throw new Error("Cannot divide by zero");
    return x / 2;
}

const safeProcess = pipeSafe(add, divide);

console.log(safeProcess(4));  // { ok: true, value: 2.5 }
console.log(safeProcess(0));  // { ok: false, error: "Cannot divide by zero" }