const http = require('http');

//Обработчик маршрутов
// const routeHandler = require('./routes/router');

//Создание HTTP сервера

const server = http.createServer((req,res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.write('<h1>Hello motherfucker </h1>');
    res.end();
});


//Запуск сервера на порту 8000
const PORT = 8000;
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});