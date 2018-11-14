{
    "targets": [{
        "target_name": "module",
        "sources": [ "./src/module.c" ],
        "library_dirs": [
          "../lib",
        ],
        'conditions': [
            ['OS!="win"',
              {
                'link_settings': {
                  'libraries': [
                    '-lavutil'
                  ]
                }
              }
            ],
            ['OS=="win"',
              {
                'link_settings': {
                  'libraries': [
                    '-../lib/lavutil.lib'
                  ],
                }
              }
            ]
        ],
        "include_dirs": [
          "<!(node -e \"require('napi-macros')\")"
        ]
    }],
}
