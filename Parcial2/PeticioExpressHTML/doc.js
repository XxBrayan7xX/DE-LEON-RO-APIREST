const express = require('express');
const app = express();
app.get("/alumnos",(req,res)=>{
    //console.log(req.params);
    //console.log(req.query);
    //console.log(req.body);//Aqui se envia un Json en el body
    res.json({respuesta: "Servidor express contestando  peticion get"})
 });
app.post("/alumnos",(req,res)=>{ 
    res.json({respuesta:"Servidor express contestando  peticion post"})
});
app.listen(8081,(req,res)=>{
    console.log("El servidor express esta escuchando...")
})