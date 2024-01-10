const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('database.db');
require('dotenv').config();

const express = require('express');
const unidecode = require('unidecode');  
const app = express();
const port = 1337;
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

const initializeDb = require('./initializeDb');

const Blacklist = ['>', '<', '=', '"', 'true', 'or', '--', 'and', 'false', ';','select','union','where',' ','admin.alphabit'];

function isBlacklisted(value, blacklist) {
    const lowercasedValue = value.toLowerCase();
    return blacklist.some(char => lowercasedValue.includes(char));
}

function cleanInput(input) {
    return unidecode(input);
}

app.post('/login', (req, res) => {
    let { username, password } = req.body;
    try {
     

        if (isBlacklisted(username, Blacklist) || isBlacklisted(password, Blacklist)) {
            return res.render('./index', { error: 'Invalid username or password', msg: '' });
        }
        username = cleanInput(username);
        const sqlQuery = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
        db.get(sqlQuery, (err, row) => {
            if (err) {
                return res.render('./index', { error: `The app crashed because of your query !! \n ${sqlQuery}`, msg: '' });
            }
            if (!row) {
                return res.render('./index', { error: 'Authentication failed', msg: 'try more harder' });
            }
            res.send(process.env.FLAG);
        });
    } catch (error) {
        res.render('./index', { error: 'Authentication failed', msg: 'f' });
    }
});

app.get('/', (req, res) => {
    res.render('./index', { error: '', msg: '' });
});

initializeDb();
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
