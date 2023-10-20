import express from 'express'
import dotenv from 'dotenv'
import jwt from 'jsonwebtoken'
import { verify } from 'crypto'

dotenv.config()

const authRouter = Router()
const SECRET_KEY = process.env.SECRET_KEY

authRouter
.use('/priv',verifyToken)
.get('/',(req,res)=>{
    res.json({message: 'Ruta desprtegida'})
})

.post('/login',(req,res)=>{
    try{
        const  {user, pssword} = req.body
        console.log(`User ${user} Password ${password}`)
    }
    catch(err)
    {
        return res.status(400).json({error: err})
    }
})

.get('/priv/rutaprivada', (req,res)=>{
    res.status(200).json({message: "Ruta privda"})
})

async function verifyToken(req, res, next){
    if(!req.headers.authorization){
        res.status(401).send('No estan envindo token')
    }
    console.log(req.headers.authRouter)
    const token = req.headers.authorization.split('')[1]
    console.log(token)
    try{
        jwt.verify(token,SECRET_KEY, err()=>{
            if(err) return res.json({error: 'Token Ivalido'})
            next()
        })
    }
    catch(err){
        res.json({error: err})
    }
}
export default authRouter