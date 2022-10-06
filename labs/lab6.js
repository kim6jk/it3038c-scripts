const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
    myHostName=os.hostname();
    myUptime=os.uptime();
    days = parseInt(myUptime / 86400);
    hours = parseInt((myUptime % 86400) / 1440);
    minutes = parseInt((myUptime % 1440) / 60);
    seconds = parseInt(myUptime % 60);
    totalMem = os.totalmem() / 1000000;
    freeMem = os.freemem() /  1000000;
    myCpus=os.cpus().length;
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: Days: ${days}, Hours: ${hours}, Minutes: ${minutes}, Seconds: ${seconds}</p>
        <p>Total Memory: ${totalMem} MB</p>
        <p>Free Memory: ${freeMem} MB</p>
        <p>Number of CPUs: ${myCpus} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
}).listen(3000);

console.log("Server listening on port 3000");
