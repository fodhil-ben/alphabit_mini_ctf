const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('database.db');
require('dotenv').config()

const express = require('express');
const app = express();
const port = 1337;
app.use(express.urlencoded({ extended: true }))
app.use(express.json())

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

const initializeDb = require('./initializeDb')


app.post('/login', (req, res) => {
    const { username, password } = req.body;

    try {
        const sqlQuery = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
        db.get(sqlQuery, (err, row) => {
            if (err) {
                return res.render('./index', { error: `the app crashed because of your query !! \n ${sqlQuery}`, msg: '' });
            }
            if (!row) {
                return res.render('./index', { error: 'Authentication failed', msg: 'kj' });
            }
            res.send(process.env.FLAG);
        });
    } catch (error) {
        res.render('./index', { error: 'Authentication failed', msg: 'f' });
    }
});


app.get('/', (req, res) => {
    res.render('./index', { error: '', msg: '' })
});

initializeDb()
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
