function groupBy(items, key) {
    return items.reduce((result, item) => {
        const groupKey = item[key];
        if (!result[groupKey]) {
            result[groupKey] = [];
        }
        result[groupKey].push(item);
        return result;
    }, {});
}

const items = [
    { id: 1, category: 'fruit', name: 'apple' },
    { id: 2, category: 'fruit', name: 'banana' },
    { id: 3, category: 'vegetable', name: 'carrot' },
];

console.log(groupBy(items, 'category'));