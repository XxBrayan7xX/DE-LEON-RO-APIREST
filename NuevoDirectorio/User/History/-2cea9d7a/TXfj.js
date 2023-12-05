const chai = require('chai');
const chaiHttp = require('chai-http');

chai.use(chaiHttp);
let app = 'http://localhost:8087'

describe("Pruebas de la ruta de usuarios",()=>{
    it("Prueba metodo get a la ruta de usuario me debe dar un status 200",()=>{
        chai.request(app)
        .get('/usuario')
    // .send({ password: '123', confirmPassword: '123' })
        .end((err, res) => {
         expect(err).to.be.null;
         expect(res).to.have.status(200);
        });
    });
});