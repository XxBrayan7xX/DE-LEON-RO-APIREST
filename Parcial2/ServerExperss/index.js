const express = require('express');
const app = express();

app.use(express.json());

app.get("/alumnos/:carrera",(req,res)=>{
    console.log(req.params);
    console.log(req.query);
    console.log(req.body);//Aqui se envia un Json en el body
    res.send("Servidor express contestando  peticion get")
 });
app.post("/alumnos",(req,res)=>{ 
    res.send("Servidor express contestando  peticion post")
});
app.listen(3000,(req,res)=>{
    console.log("El servidor express esta escuchando...")
})