#include <node_api.h>
#include <napi-macros.h>
#include <stdio.h>
#include <stdlib.h>
#include "lzo.h"

#define BUFFER_SIZE 200

NAPI_METHOD(decompress) {
  NAPI_ARGV(2)
  NAPI_ARGV_BUFFER(in, 0)
  NAPI_ARGV_INT32(length, 1)

  int outlen = BUFFER_SIZE;
  unsigned char *out = malloc(outlen);
  napi_value result;

  int ret = av_lzo1x_decode(out, &outlen, in, &length);
  int size = BUFFER_SIZE - outlen;

  if (ret != 0) {
    napi_throw_error(env, NULL, "Failed to decompress");
  }

  NAPI_STATUS_THROWS(napi_create_buffer_copy(env, size, out, NULL, &result));

  free(out);

  return result;
}

NAPI_INIT() {
  NAPI_EXPORT_FUNCTION(decompress)
}
