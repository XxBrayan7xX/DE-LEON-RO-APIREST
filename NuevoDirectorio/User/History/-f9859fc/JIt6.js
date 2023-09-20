const events = require('events');

function saludar(){
    const emisor = new events.EventEmitter();
    setTimeout(()=>emisor.emit('saluda','Juan'),5000);
    setTimeout(()=>emisor.emit('saluda','Pedro'),3000);
    setTimeout(()=>emisor.emit('saluda','Martin'),7000);
    return emisor;
}
let sal = saludar();

sal.on('saluda',(nombre)=>{
    console.log('Hola'+nombre)
});

// emisor.addListener('Saluda',(nombre)=>{
//     console.log('Hola'+nombre)
// });



