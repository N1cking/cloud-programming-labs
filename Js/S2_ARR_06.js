function transformRecords(users) {
    return users
        .filter(user => user.active)
        .map(user => user.name.toUpperCase())
        .sort();
}

const users = [
    { id: 1, name: "Alice", active: true },
    { id: 2, name: "Bob", active: false },
    { id: 3, name: "Charlie", active: true },
    { id: 4, name: "David", active: false },
];

console.log(transformRecords(users));  // ["ALICE", "CHARLIE"]