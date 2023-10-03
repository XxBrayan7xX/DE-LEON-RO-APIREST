
const express = require('express');
const { check,validationResult } = require('express-validator')
const app = express();
app.use(express.json());

app.post("/usuario",[check('edad').isNumeric(),check('correo').isEmail()],(req,res)=>{
    const result = validationResult(req);
    if (result.isEmpty()) {
        console.log(req.body);
        res.json({mensaje:"Respuesta a peticion post"});
      }
      else{
        res.json(result);
      }
});

// app.get('/usuario', query('person').notEmpty(), (req, res) => {
//   const result = validationResult(req);
//   if (result.isEmpty()) {
//     return res.send(`Hello, ${req.query.person}!`);
//   }

//   res.send({ errors: result.array() });
// });
app.listen(8081,()=>{
    console.log("Servidor express escuchando")
});