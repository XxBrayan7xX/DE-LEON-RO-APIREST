const express = require('express');
const morgan = require('morgan');
const fs = require('fs')
const path = require('path');
var mysql = require('mysql2');

  var app = express()
 
// create a write stream (in append mode)
var accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' })
 
app.get("/usuarios", async(req,res)=>{
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
    res.status(404).json({mensaje:"el usuario no existe"})
  }
  else{
    res.json(rows)
  }
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