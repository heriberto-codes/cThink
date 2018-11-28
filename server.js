const express = require('express');
const app = express();

// serve our index.html file, use express static middleware function
app.use(express.static('public'));
app.listen(process.env.PORT || 8080); 
