const user = { name: "Ala", tags: [] };

user.tags.push("tag1");
user.tags.push("tag2");

console.log(user); 

try {
    
    user = {}; // For errorcing an error
} catch (error) {
    console.log("Error: " + error.message);
}