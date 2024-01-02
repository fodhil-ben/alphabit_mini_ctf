const express = require('express');
const app = express();
const port = 1335;
const axios = require('axios')

app.use(express.urlencoded({ extended: true }))
app.use(express.json())

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

async function checkWebsite(url) {
    try {
        const result = await axios(url);
        return { msg: result.data, error: '' }
    } catch (error) {
        return { msg: '', error: 'Error happened Try again!!' }
    }
}

app.post('/view', async (req, res) => {
    const { url } = req.body;
    const { msg, error } = await checkWebsite(url)
    res.render('./index', { msg, error });
});

app.get('/', (req, res) => {
    res.render('./index', { msg: '', error: '' })
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
