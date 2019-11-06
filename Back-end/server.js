const express = require('express');
const app = express();

var weight = 0.0

app.get('/',(req,res)=>{
    console.log(req.query);
    var json = {
        weight : weight,
    };
    res.send(JSON.stringify(json));
});

app.get('/setWeight',(req,res)=>{
    weight = req.query.weight;
    res.send('ok');
});

app.listen(27580,(req,res)=>{
    console.log('running');
});