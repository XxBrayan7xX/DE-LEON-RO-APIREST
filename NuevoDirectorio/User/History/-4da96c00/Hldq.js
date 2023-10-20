const yaml = require('yaml');
const fs = require('fs');
const path = require('path');

const archivoObj = fs.readFileSync(path.join(__dirname,'/ArchivosYAML/archivo.yaml'));
const valorObj = yaml.parse(archivoObj);
console.log(valorObj);