{
    "targets": [{
        "target_name": "module",
        "sources": [ "./src/module.c" ],
        "library_dirs": [
          "../lib",
        ],
        "conditions": [ [ "OS!='win'", {
            "libraries": [
                "-lavutil"
            ],
        } ] ],
        'msvs_settings': {
          'VCLinkerTool': {
            'AdditionalLibraryDirectories': [
              '../lib'
            ],
          },
        },
        "include_dirs": [
          "<!(node -e \"require('napi-macros')\")"
        ]
    }],
}
