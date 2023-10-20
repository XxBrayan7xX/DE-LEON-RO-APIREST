const express = require('express');
const https = require('https');
const fs = require('fs');
const path =  require('path');
const app = express();
const opciones  = {
    key: fs.readFileSync(path.join(__dirname,"ssl/key.pem")),
    cert: fs.readFileSync(path.join(__dirname,"ssl/cert.pem"))//Se puede probar poneindo esto entre consol.log
}
app.get("/",(req,res)=>{
    res.send("Servidor express contestando  peticion get")
 });

 https.createServer(opciones, app).listen(8082, function(){
    console.log("Servidor Express Seguro en puerto 8082...")
 })

//  app.listen(8081,(req,res)=>{
//     console.log("El servidor express esta escuchando...")
// })