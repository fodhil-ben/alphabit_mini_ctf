const mongoose = require('mongoose')
require('dotenv').config()
const express = require('express');
const app = express();
const port = 1330;

app.use(express.urlencoded({ extended: true }))
app.use(express.json())

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');


(async function () {

    const userSchema = new mongoose.Schema({
        username: String,
        password: String
    })
    try {
        db = mongoose.connect(process.env.DB_URI)
        console.log('connected successfully')
    } catch (error) {
        console.log('error connecting to the database')
    }
    const User = mongoose.model('User', userSchema)
    try {
        let found = await User.findOne({ username: "admin" });
        if (!found) {
            const adminUser = new User({ username: "admin", password: process.env.PASSWORD })
            adminUser.save()
        }
    } catch (error) {
        console.log('error getting admin user')
    }

    app.post('/login', async (req, res) => {
        const { username, password } = req.body;
        try {
            console.log(username, password)
            const userFound = await User.findOne({ username, password })
            if (!userFound) {
                return res.render('./index', { error: 'Authentication failed', msg: '' });
            }
            res.render('./index', { error: '', msg: process.env.FLAG });
        } catch (error) {
            res.render('./index', { error: 'Authentication failed', msg: '' });
        }
    });

    app.get('/', (req, res) => {
        res.render('./index', { error: '', msg: '' })
    });
    // app.get('/all', async (req, res) => {
    //     const users = await User.find({ username: 'admin' })
    //     console.log(users)
    //     res.render('./index', { error: '', msg: users })
    // });

    app.listen(port, () => {
        console.log(`Server is running at http://localhost:${port}`);
    });

})();