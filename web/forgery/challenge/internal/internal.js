require('dotenv').config()
const express = require('express');
const app = express();
const port = 8080;

app.get('/flag', (req, res) => {
    res.send(`GG here is you flag: ${process.env.FLAG}`)
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}/flag`);
});
