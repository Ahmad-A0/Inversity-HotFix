const express = require('express');
const app = express();
const port = 3000;

const catNames = [
  "Whiskers",
  "Mittens",
  "Fluffy",
  "Snowball",
  "Purrfect",
  "Kitty",
  "Meowzer",
  "Luna",
  "Ginger",
  "Simba"
];

app.get('/api/cat-names', (req, res) => {
  res.json(catNames);
});

app.listen(port, () => {
  console.log(`Meowazon Web Services listening on port ${port}`);
});

