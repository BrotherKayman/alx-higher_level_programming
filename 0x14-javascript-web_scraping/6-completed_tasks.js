#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Error code:', response.statusCode);
    return;
  }

  const tasks = JSON.parse(body);
  const CompletedTaskByID = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!CompletedTaskByID[task.userId]) {
        CompletedTaskByID[task.userId] = 1;
      } else {
        CompletedTaskByID[task.userId]++;
      }
    }
  });

  console.log(CompletedTaskByID);
});
