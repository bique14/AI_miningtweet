// helloWorld.js
var http = require("http");

http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/html'});
  response.write('Hello World<br>');
  for (i=0;i<5;i++){
      response.write(String(i)+"<br>");
  }
  response.end('Bye!');
}).listen(3000);

console.log('Server running at http://127.0.0.1:3000/');
