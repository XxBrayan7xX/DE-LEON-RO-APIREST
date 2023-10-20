const yaml = require('yaml');
const fs = require('fs');
const path = require('path');

const archivoObj = fs.readFileSync(path.join(__dirname,'/archivo.yml'),'utf8');
const valorObj = yaml.parse(archivoObj);
console.log(valorObj);