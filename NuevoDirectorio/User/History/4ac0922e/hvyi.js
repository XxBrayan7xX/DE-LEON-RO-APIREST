const express = require('express');
const { check,validationResult, checkSchema } = require('express-validator')
const app = express();
app.use(express.json());

app.post("/usuario",checkSchema({
  'nombre':{isLength:{options:{min:5,max:10}}},
  'edad':{isNumeric:{errorMessage:"Edad debe ser numerica"}},
  'correo': {isEmail: {errorMessage:"Debe ser un correo valido como ejemplo@gmail.com"}
}),(req,res)=>{
    const result = validationResult(req);
    if (result.isEmpty()) {
        console.log(req.body);
        res.json({mensaje:"Respuesta a peticion post"});
      }
      else{
        res.json(result);
      }
});


app.listen(8081,()=>{
    console.log("Servidor express escuchando")
});