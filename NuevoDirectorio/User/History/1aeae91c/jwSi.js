const express = require('express');
const morgan = require('morgan');
const fs = require('fs')
const path = require('path');
var mysql = require('mysql2');
var cors = require('cors');
const basicAuth = require('express-basic-auth')
const bearerToken = require('express-bearer-token');

  var app = express()
 
app.use(cors());
// create a write stream (in append mode)
//app.use(bearerToken());
//app.use(function (req, res) {
  //res.send('miTOken '+req.token);
//});






// app.use(basicAuth({
//   users: { 'admin': '1234' }
// }))

var accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' })
 
app.get("/usuarios", async(req,res)=>{
  req.token
  try {
    const conn = await mysql.createConnection({host:'localhost',user:'prueba',password:'prueba',database:'serverbd', port: 3307})
    const [rows, fields] = await conn.promise().query('SELECT * FROM ALUMNOS')
    res.json(rows)
  } catch (err){
    //console.log(err)
    res.status(500).json({mensaje:err.sqlMessage})
  }



})
 app.get("/usuarios/:id", async(req,res)=>{
  console.log(req.params.id)
  const conn = await mysql.createConnection({host:'localhost',user:'prueba',password:'prueba',database:'serverbd', port:3307})
  const [rows, fields] = await conn.promise().query('SELECT * FROM ALUMNOS where matricula='+req.params.id)
  if(rows.length==0){
    //res.status(404).json({mensaje:"el usuario no existe"})
    let e = new Error("Error del lado de usuario")
    next(e)
  }
  else{
    res.json(rows)
  }
})
app.use((err,req,res,next)=>{
  res.status(404)
  res.send({Error: err.mensaje})
})
app.delete("/usuarios", async(req,res)=>{
  console.log(req.query)
  try {
    const conn = await mysql.createConnection({host:'localhost',user:'prueba',password:'prueba',database:'serverbd', port: 3307})
    const [rows, fields] = await conn.promise().query(`delete FROM ALUMNOS WHERE Matricula = ${req.query.idUsuario}`)
    if(rows.affectedRows==0){
      res.json({mensaje:"Registro no eliminado"})
    }else{res.json({mensaje: "Alumno eliminado"})}

    //res.json(rows)
  } catch (err){
    res.status(500).json({mensaje:err.sqlMessage})
  }
})

app.patch("/usuarios")

app.use(express.json())
app.get("/alumnos", (req,res)=>{
    res.send("servidor express contestando a peticion get")
})
app.post("/alumnos", (req,res)=>{
    res.send("servidor express contestando a peticion post")
})


app.listen(8081,(req,res)=>{
    console.log("El servidor express esta escuchando...")
})

