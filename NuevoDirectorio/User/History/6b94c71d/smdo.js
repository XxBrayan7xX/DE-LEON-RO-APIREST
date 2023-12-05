const express = require('express');
const morgan = require('morgan');
const fs = require('fs')
const path = require('path');
var mysql = require('mysql2');
const redoc = require('redoc-express');
//const basicAuth = require('express-basic-auth')
//const bearerToken = require('express-bearer-token');
const swaggerUI = require('swagger-ui-express');
const swaggerJsDoc = require('swagger-jsdoc');

const { SwaggerTheme } = require('swagger-themes');
const theme = new SwaggerTheme('v3');

const options = {
  explorer: true,
  customCss: theme.getBuffer('feeling-blue')
};

var app = express()
const def = fs.readFileSync(path.join(__dirname,'./swagger.json'),
  {encoding: 'utf-8', flag:'r'});
const read =fs.readFileSync(path.join(__dirname,'./README.MD'),
  {encoding: 'utf8',flag:'r'})
const defObj = JSON.parse(def)
defObj.info.description=read

const swaggerOptions = {
  definition:defObj,
  apis: [`${path.join(__dirname,"doc.js")}`],
}


// create a write stream (in append mode)
//app.use(bearerToken());
//app.use(function (req, res) {
  //res.send('miTOken '+req.token);
//});






// app.use(basicAuth({
//   users: { 'admin': '1234' }
// }))

var accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' })
/**
 * @swagger
 * /usuarios/:
 *   get:
 *     tags:
 *       - usuario
 *     summary: Consultar todos los usuarios
 *     description: Obtiene un JSON conteniendo todos los usuarios de la BD
 *     responses:
 *       200:
 *         description: Regresa un JSON conteniendo todos los usuarios de la BD
 */

 
app.get("/usuarios", async(req,res)=>{
  req.token
  try {
    const conn = await mysql.createConnection({host:'localhost',user:'prueba',password:'prueba',database:'serverbd', port: 3307})
    const [rows, fields] = await conn.promise().query('SELECT * FROM ALUMNOS')
    res.json(rows)
  } catch (err){
    res.status(500).json({mensaje:err.sqlMessage})
  }



})
 app.get("/usuarios/:id", async(req,res,next)=>{
  try{
  console.log(req.params.id)
  const conn = await mysql.createConnection({host:'localhost',user:'prueba',password:'prueba',database:'serverbd', port:3307})
  const [rows, fields] = await conn.promise().query('SELECT * FROM ALUMNOS where matricula='+req.params.id)
  if(rows.length==0){
    let e = new Error("Error del lado de usuario, id inexistente.")
    next(e)
  }
  else{
    res.json(rows)
  }
}
catch{
  let e = new Error("No es posible establecer la conexion")
  next(e)
}
})
app.use((err,req,res,next)=>{
  res.status(500)
  res.send({Error: err.message})
})
const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use("/api-docs",swaggerUI.serve,swaggerUI.setup(swaggerDocs,options));
app.use("/api-docs-json",(req,res)=>{
  res.json(swaggerDocs);
});

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


app.get(
  '/docs',
  redoc({
    title: 'API Docs',
    specUrl: '/api-docs-json',
    nonce: '', // <= it is optional,we can omit this key and value
    // we are now start supporting the redocOptions object
    // you can omit the options object if you don't need it
    // https://redocly.com/docs/api-reference-docs/configuration/functionality/
    redocOptions: {
      theme: {
        colors: {
          primary: {
            main: '#6EC5AB'
          }
        },
        typography: {
          fontFamily: `"museo-sans", 'Helvetica Neue', Helvetica, Arial, sans-serif`,
          fontSize: '15px',
          lineHeight: '1.5',
          code: {
            code: '#87E8C7',
            backgroundColor: '#4D4D4E'
          }
        },
        menu: {
          backgroundColor: '#ffffff'
        }
      }
    }
  })
);


app.listen(8087,(req,res)=>{
    console.log("El servidor express esta escuchando...")
})

fetch("http://localhost:8087/api-docs-json")
  .then(respuesta=>respuesta.json())
    .then(desc=>{
const openApi = desc // Open API document
const targets = ['node_unirest', 'c'] // array of targets for code snippets. See list below...

try {
  // either, get snippets for ALL endpoints:
  const results = OpenAPISnippet.getSnippets(openApi, targets) // results is now array of snippets, see "Output" below.
  console.log(result)
  // ...or, get snippets for a single endpoint:
  const results2 = OpenAPISnippet.getEndpointSnippets(openApi, '/users/{user-id}/relationship', 'get', targets)
} catch (err) {
  // do something with potential errors...
}
})

