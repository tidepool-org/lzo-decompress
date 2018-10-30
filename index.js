const binding = require('node-gyp-build')(__dirname);
const fs = require('fs');

fs.readFile('y.lzo', (err, data) => {
  if (err) throw err;
  var skip = 0x32;
  let ret = binding.decompress(data.slice(skip), data.length - skip);
  console.log('Decoded:', ret.toString());
});

module.exports = binding;
