const fs = require('fs');
const path = require('path');
const express = require('express');
const app = express();

app.use(express.static('pub'));
app.listen(3000, () => {
    console.log("Escuchando en: http://localhost:3000")
});
app.get('/', (request, response) => {
    response.sendFile(path.resolve(__dirname, 'index.html'))
});
// ruta para ver archivos
app.get('/archivos', (request, response) => {
    fs.readdir('./archivos', (error, files) => {
        if(error){
            console.error(err);
            response.status(500).send('Error al mostrar archivos');
        }else{
            const misArchivos = files.map((file) => file.split('.')[0]);
            console.log(misArchivos);
            response.send(misArchivos);
        }
    });
});

/*
// Crear un Archivo
app.post('/archivos', (request ,response) => {
    const nombre = request.body.nombre;
    const contenido = request.body.contenido;

    fs.access(`./archivos/${titulo}.md`, fs.constants.F_OK, (err) => {
        if(!err) {
            response.status(409).send('El archivo ya existe');
        }else {
            const archivoData = `${nombre}\n${contenido}`;

            fs.writeFile(`./archivos/${titulo}.md`, archivoData, 'utf8', (err) => {
                if(err) {
                    console.error(err);
                    response.status(500).send('Error al crear archivo');
                } else {
                    response.redirect('/');
                }
            })
        }
    })
});
*/
/* // Para convertir de markdown a html?
const fs = require('fs')
const path = require('path')
const express = require('express')
const bp = require('body-parser')
const MarkdownIt = require('markdown-it'),
    md = new MarkdownIt();
const app = express()

app.use(express.static('pub'))
app.use(bp.json())
app.use(bp.urlencoded({
    extended: true
}))

app.listen(3000, () => {
    console.log("Escuchando en: http://localhost:3000")
})

app.get('/', (request, response) => {
    response.sendFile(path.resolve(__dirname, 'index.html'))
})

app.post('/', (request, response) => {
    console.log(request.body)
    let markDownText = request.body.text
    console.log(markDownText)
    let htmlText = md.render(markDownText)
    response.setHeader('Content-Type', 'application/json')
    response.end(JSON.stringify({
        text: htmlText
    }))
})
 */
