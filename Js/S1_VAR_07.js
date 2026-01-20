function toNumberOrNull(x) {
    const result = +x;  // Преобразуем строку в число с помощью унарного плюса
    return isNaN(result) ? null : result;
}

console.log(toNumberOrNull("12"));    // 12
console.log(toNumberOrNull("12.5"));  // 12.5
console.log(toNumberOrNull(" 12 "));  // 12
console.log(toNumberOrNull("12x"));   // null
console.log(toNumberOrNull(""));      // null