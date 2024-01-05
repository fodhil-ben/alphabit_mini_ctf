const express = require('express');
const app = express();
const port = 1336;
app.get('/', (req, res) => {
    res.send('you cant GET any thing try to POST something ..')
});
app.post('/', (req, res) => {
    if (req.headers['user-agent'] === 'l33t_br0w$3r') {
        if (req.headers['authorization'] === 'authorised') {
            if (req.headers['content-language'] === 'arabic') {
                if (req.headers['location'] === 'alphabit') {
                    res.send('Alphabit{GG_Y0u_kn0w_HTTP_headers_y0u_4r3_7h3_b3s7_h34d3rs_hun73r}')
                }
                else {
                    res.send('to get the flag your location must be in alphabit :) ')
                }
            } else {
                res.send('the content must be in arabic')
            }
        } else {
            res.send('You must be authorised to get the flag')
        }
    } else {
        res.send('only users that uses our l33t_br0w$3r can access our leet website')
    }
});


app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
