let mocha = require('mocha');
let chai = require('chai');
let expect = chai.expect;
var describe = mocha.describe;
let modulo = require('../src/modulo.js');

describe('Pruebas de validcion con Mocha areaTriangulo',()=>{
    it('Si le mando un 2 y 3 deberia darme 3',()=>{
        let resultado = modulo.areaTriangulo(2,3);
        expect(resultado).to.be.a('number');
        expect(resultado).to.equal(3);
    });
});