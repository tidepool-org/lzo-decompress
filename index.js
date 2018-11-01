const binding = require('node-gyp-build')(__dirname);
const fs = require('fs');

fs.readFile('./LZO/cgm-history-compressed.bin', (err, data) => {
  if (err) throw err;
  console.log('Encoded length:', data.length);
  let ret = binding.decompress(data, 4096);
  console.log('Decoded.');
  fs.readFile('./LZO/cgm-history-uncompressed.bin', (err, uncompressed) => {
    console.log('Compared:',ret.compare(uncompressed));
  });
});

module.exports = binding;
