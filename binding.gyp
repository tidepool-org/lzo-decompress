{
    "targets": [{
        "target_name": "module",
        "sources": [ "./src/module.c" ],
        "libraries": [
            "-Wl,-rpath,./lib"
        ],
        "include_dirs": [
          "<!(node -e \"require('napi-macros')\")"
        ]
    }],
}
