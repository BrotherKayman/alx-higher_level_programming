#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node writeToFile.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
