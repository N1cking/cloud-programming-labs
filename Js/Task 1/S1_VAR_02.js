try {
    {
        let myVarLet = "I am inside a block!";
        console.log(myVarLet); // Можно вывести переменную внутри блока
    }
    console.log(myVarLet); // Попытка вывести переменную за пределами блока
} catch (error) {
    console.log("Error with let: " + error.message);
}

try {
    {
        var myVarVar = "I am inside a block!";
        console.log(myVarVar); // Можно вывести переменную внутри блока
    }
    console.log(myVarVar); // Можно вывести переменную за пределами блока
} catch (error) {
    console.log("Error with var: " + error.message);
}

console.log("Explanation:");
console.log("let is block-scoped and not accessible outside the block.");
console.log("var is function-scoped and accessible outside the block.");