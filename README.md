# lzo-decompress

Use LZO for decompression on Node.js

## Introduction

`lzo-decompress` is an [N-API](https://nodejs.org/api/n-api.html) wrapper around the LZO implementation of [FFMpeg's libavutil](https://github.com/FFmpeg/FFmpeg/tree/master/libavutil) library. It uses version 3 of N-API which is [only available](https://nodejs.org/api/n-api.html#n_api_n_api_version_matrix) on Node v10 and higher. v0.1.2 works in Electron v3, while v1.0.0 works in Electron v4 and higher.

This software uses code of [FFmpeg](http://ffmpeg.org) licensed under the [LGPLv3](https://www.gnu.org/licenses/lgpl.html) and its source can be downloaded [here](https://github.com/FFmpeg/FFmpeg/tree/master/libavutil).

## Usage

```
const lzo = require('lzo-decompress');

lzo.decompress(input, length);
```

## Building from source

- `yarn prebuild`
- `yarn prebuild-ia32` (for 32-bit versions)

On macOS, you may need to do `brew install ffmpeg` first.

## Instructions for Tidepool engineers

### Updating on Yarn/NPM

The following steps will update the module on Yarn/NPM:

- `yarn version`
- `git push && git push --tags`
- Wait for Travis to finish.
- Download the releases from Github: `prebuildify-ci download`
- `npm publish`

Note that you need to `yarn global add prebuildify-ci` to get the prebuilds.

### Building ffmpeg

If for some reason you need to rebuild the shared libraries, use the [ffmpeg-windows-build-helpers](https://github.com/rdp/ffmpeg-windows-build-helpers) script to build LGPL-licensed 32-bit and 64-bit cross-compiled shared libraries as follows:

```
./cross_compile_ffmpeg.sh --enable-gpl=n --build-ffmpeg-shared=y --compiler-flavors=multi
```
