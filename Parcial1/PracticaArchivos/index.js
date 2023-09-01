const fsc = require('fs');
const path = require('path');
const {jsPDF} = require("jspdf")
var x1 = require('excel4node');

fsc.writeFile(path.join(__dirname, 'archivoo.txt'), "archivo creado con api callback", (err)=>{
    if(err){
        console.log(err)
    }else{
        console.log("Archivo credo con el API callbaack")
    }
});
//PDF
const doc = new jsPDF();
doc.text("Hello world",10,10);
doc.save(path.join(__dirname,"miPDF.pdf"));

//XLSX
var wb = new x1.Workbook();
var ws = wb.addWorksheet('Sheet 1');
var ws2 = wb.addWorksheet('Sheet 2');

// Create a reusable style
var style = wb.createStyle({
  font: {
    color: '#FF0800',
    size: 12,
  },
  numberFormat: '$#,##0.00; ($#,##0.00); -',
});

// Set value of cell A1 to 100 as a number type styled with paramaters of style
ws.cell(1, 1)
  .number(100)
  .style(style);

  wb.write(path.join(__dirname,'Excel.xlsx'));