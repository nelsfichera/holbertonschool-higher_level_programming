#!/usr/bin/node
const request = require('request');
const GET = request.get;
const url = process.argv[2];

GET(url, (err, res, body) => {
  if (err) return (console.log(err));
  const data = JSON.parse(body);
  const tasks = {};

  for (let x = 0; x < data.length; x++) {
    if (data[x].completed) {
      const id = data[x].userId;
      tasks[id] !== undefined ? tasks[id] += 1 : tasks[id] = 1;
    }
  }
  console.log(tasks);
});
