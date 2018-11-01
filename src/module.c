#include <node_api.h>
#include <napi-macros.h>
#include <stdio.h>
#include <stdlib.h>
#include "lzo.h"

NAPI_METHOD(decompress) {
  NAPI_ARGV(2) // there are two arguments passed in
  NAPI_ARGV_BUFFER(inputBuffer, 0)
  NAPI_ARGV_INT32(outputBufferSize, 1)

  unsigned char *outputBuffer = malloc(outputBufferSize);
  int remaining = outputBufferSize;
  napi_value result;
  int inputBufferSize = inputBuffer_len; // set by NAPI_ARGV_BUFFER

  int ret = av_lzo1x_decode(outputBuffer, &remaining, inputBuffer, &inputBufferSize);

  if (ret != 0) {
    napi_throw_error(env, NULL, "Failed to decompress");
  }

  NAPI_STATUS_THROWS(napi_create_buffer_copy(env, outputBufferSize, outputBuffer, NULL, &result));

  free(outputBuffer);

  return result;
}

NAPI_INIT() {
  NAPI_EXPORT_FUNCTION(decompress)
}
