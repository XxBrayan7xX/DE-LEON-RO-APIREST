const express = require('express');
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const folder = path.join(__dirname+'/archivos/');

const storage = multer.diskStorage({
    destination: function(req, file,cb){cb(null, folder)},
    filename: function(req, file, cb){cb(null, folder.originlaname)}
});
const upload = multer({storage:storage})
const app = express();
app.use(cors());
app.use(express.urlencoded({extended:true}))
//app.use(express.json());

app.get("/alumnos/:carrera",(req,res)=>{
    console.log(req.params);
    console.log(req.query);
    console.log(req.body);//Aqui se envia un Json en el body
    res.send("Servidor express contestando  peticion get")
 });
// app.post("/alumnos",(req,res)=>{ 
//     res.send("Servidor express contestando  peticion post")
// });
app.post('/usurio/',(req,res)=>{
    console.log('Se recibio el formulrio: '+ JSON.stringify(req.body))
});
app.listen(3000,(req,res)=>{
    console.log("El servidor express esta escuchando...")
})