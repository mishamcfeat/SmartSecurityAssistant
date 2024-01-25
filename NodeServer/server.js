const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Node.js server for Smart Security Assistant');
  // [Code to handle data from Arduino Hub and interact with InfluxDB]
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});