const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('database.db');

const initializeDb = () => {
    const insertUserQuery = 'INSERT INTO users (username, password) VALUES (?, ?)';
    db.serialize(() => {
        db.run(`
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
        )
        `);
        db.run(insertUserQuery, ['admin.alphabit', '$#@3L!0p9Pw#Rfdkjfdshfjhuehwfj'], (err) => {
            if (err) {
                console.error('Error initializing users:', err.message);
            }
        });
        console.log('success: db initialized')
    })
};

module.exports = initializeDb