const express = require('express')
const path = require('path');
PORT = 1333
app = express()

app.get('/', (req, res) => {
    res.cookie('part_2/3_of_the_flag', 'Y0U_4R3_4_R3')
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
app.get('/robots.txt', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'robots.txt'));
});
app.get('/super_secret_file.txt', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'super_secret_file.txt'));
});

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
})