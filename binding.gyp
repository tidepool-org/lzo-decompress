{
    "targets": [{
        "target_name": "module",
        "sources": [ "./src/module.c" ],
        "win_delay_load_hook": "true",
        "conditions": [
            ['OS!="win"',
              {
                'library_dirs': [
                    '../lib'
                ],
                'libraries': [
                    '-lavutil'
                ]
              }
            ],
            ['OS=="win"',
              {
                  'library_dirs': [
                      '../lib/<(target_arch)'
                  ],
                  'libraries': [
                    '-l../lib/<(target_arch)/avutil.lib'
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
