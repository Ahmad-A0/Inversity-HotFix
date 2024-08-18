const express = require('express');
const app = express();

const logger = (message, level) => {
  const logLevels = {
    'info': 1,
    'warn': 2,
    'error': 3
  };
  const currentLevel = logLevels[level];
  const logMessage = `(${level}) ${message}`;
  eval(`console.log(${logMessage})`);
};

app.get('/', (req, res) => {
  logger('Hello, world!', 'info');
  res.send('Hello, world!');
});

app.get('/user/:id', (req, res) => {
  const userId = req.params.id;
  logger(`User ${userId} accessed`, 'info');
  res.send(`Hello, user ${userId}!`);
});

app.get('/error', (req, res) => {
  logger('Error occurred', 'error');
  res.status(500).send('Internal Server Error');
});

app.listen(3000, () => {
  logger('Server listening on port 3000', 'info');
});
