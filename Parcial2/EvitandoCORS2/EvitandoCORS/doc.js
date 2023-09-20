const express = require('express');
const morgan = require('morgan');
const fs = require('fs')
const path = require('path');
const mysql = require('mysql')

var app = express()
 
// create a write stream (in append mode)
var accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' })
 
// setup the logger
app.use(morgan('combined', { stream: accessLogStream }))

app.use("/alumnos",(req,res)=>{
    var mysql      = require('mysql');
    var connection = mysql.createConnection({
     host     : 'localhost',
     user     : 'me',
    password : 'secret',
    database : 'my_db'
    });
    connection.connect();
 
    connection.query('SELECT 1 + 1 AS solution', function (error, results, fields) {
      if (error) throw error;
      console.log('The solution is: ', results[0].solution);
    });
     
    connection.end();
    
    res.jsonp(results);
 });
 

app.listen(8081,(req,res)=>{
    console.log("El servidor express esta escuchando...")
})