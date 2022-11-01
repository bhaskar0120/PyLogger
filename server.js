const express = require('express');
const app = express();


app.get('/key:key', (req,res)=>{
  const ip  = req.headers['x-forwarded-for'] || req.socket.remoteAddress
  console.log(`${ip} : Pressed ${req.params.key}`);
  res.send('');
});

app.listen(3000, ()=>{
  console.log("Server listening on port 3000\n");
});
