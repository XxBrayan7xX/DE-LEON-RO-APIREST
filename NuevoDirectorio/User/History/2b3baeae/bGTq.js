const express = require('express');
const dotenv = require('dotenv');
const authRouter = require('./auth.js');

dotenv.config({path:"C:/wamp64/www/DELEONRO/Parcial2/ServidorJWT/.env"});

const app = express();
const PORT = process.env.PORT;

app.use(express.urlencoded({ extended: true }));

app.use(express.json())
    .use('/',authRouter.authRouter)
    .get('/notlogin',(req,res)=>{
        res.status(200).json({message:"No esta logueado aun, Eres un invitado en esta ruta"})
    })
    .listen(PORT,()=>{
        console.log('Servidor corriendo en el puerto - ' + PORT);
    }
)