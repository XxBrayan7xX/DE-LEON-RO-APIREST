const express = require('express');
const server = require('./server');
const app = express();

app.use('/server',server.router);
app.listen(8081,function(err){
    if(err) console.log(err);
    console.log("Servidor escuchando en puerto 8081")
})