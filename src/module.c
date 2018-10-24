#include <node_api.h>
#include <napi-macros.h>
#include <stdio.h>
#include "lzo.h"

NAPI_INIT() {
  printf("%d\n", AV_LZO_OUTPUT_PADDING);

/*
  NAPI_EXPORT_FUNCTION(attach)
  NAPI_EXPORT_FUNCTION(getFile)
  NAPI_EXPORT_FUNCTION(getFileListing)
  NAPI_EXPORT_FUNCTION(release)
*/
}
