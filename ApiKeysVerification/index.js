'use strict'

const express = require('express');
const app = express();

const accessKeys = ['393A7FE53C969A6759369E81679012ACCB4DF9C4C0E5F0393F1CA2087D70A18C']

app.get('/api/:accesshash/', (req, res) => {
    console.log(accessKeys.includes(req.params.accesshash));
    res.json({ result: accessKeys.includes(req.params.accesshash) })
})

app.listen(3001, () => { console.log('Listening on port 3001') })