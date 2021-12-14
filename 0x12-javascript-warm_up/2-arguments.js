#!/usr/bin/node
const argmnt = process.argv.length;
if (argmnt === 2) {
  console.log('No argument');
} else if (argmnt === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
