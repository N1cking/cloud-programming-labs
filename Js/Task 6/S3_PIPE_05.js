function parse(line) {
    const parts = line.split(": ");
    return { level: parts[0], message: parts[1] };
}

function filterInfo(lines) {
    return lines.filter(line => line.startsWith("INFO"));
}

function extractUserId(lines) {
    return lines.map(line => {
        const parsed = parse(line);
        const match = parsed.message.match(/user=(\d+)/);
        return match ? match[1] : null;
    }).filter(id => id !== null);
}

function pipe(...fns) {
    return x => fns.reduce((v, f) => f(v), x);
}

const logLines = [
    "INFO: user=42",
    "ERROR: something went wrong",
    "INFO: user=99",
    "WARN: warning message",
    "INFO: user=18"
];

const processLogLines = pipe(
    filterInfo,
    extractUserId
);

console.log(processLogLines(logLines));  // ["42", "99", "18"]