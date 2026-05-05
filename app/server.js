const http = require('http');

http.createServer((req, res) => {
  res.end("Version 2 🚀");
}).listen(3000, "0.0.0.0");
