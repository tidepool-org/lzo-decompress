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
                  'libraries': [
                    '-l../lib/avutil.lib'
                  ],
                  'copies': [
                      {
                        'destination': '$(SolutionDir)$(ConfigurationName)',
                        'files': [
                          '<(module_root_dir)/lib/<(target_arch)/avutil-56.dll'
                        ]
                      }
                  ]
              }
            ]
        ],
        "include_dirs": [
          "<!(node -e \"require('napi-macros')\")"
        ]
    }],
}
