const express = require('express');
const router = express.Router();

router.get('/usuarios',function(req,res){
    res.status(200).json({respuesta:"Respuesta a peticion GET"})
})
router.post('/usuarios',function(req,res){
    res.status(200).json({respuesta:"Respuesta a peticion POST"})
})
router.PUT('/usuarios',function(req,res){
    res.status(200).json({respuesta:"Respuesta a peticion PUT"})
})
router.delete('/usuarios',function(req,res){
    res.status(200).json({respuesta:"Respuesta a peticion DELETE"})
})