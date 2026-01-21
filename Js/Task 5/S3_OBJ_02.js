function mergeDefaults(defaults, overrides) {
    return { ...defaults, ...overrides };
}

const defaults = { host: "localhost", port: 3000 };
const overrides = { port: 8080 };

console.log(mergeDefaults(defaults, overrides));  // { host: "localhost", port: 8080 }