const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Frontend server running at http://localhost:${PORT}`);
});
