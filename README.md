# isara-linters

Custom linters created by ISARA to help ensure code quality.

For more information about ISARA's quantum resistant solutions, visit
our website: [www.isara.com](https://www.isara.com).

You can also contact us directly at
[quantumsafe@isara.com](mailto:quantumsafe@isara.com).

Copyright &copy; 2017-2020 ISARA Corporation, All Rights Reserved.

## Custom Linters

Our development team uses various tools to help ensure the quality of our code.
These include some simple linters that get called when submitting code reviews.

* `copyright_linter.py` - Ensure that the [Doxygen](http://doxygen.nl/)
  `@copyright` directive includes the current year.
* `doxygen_file_linter.py` - Ensure that the [Doxygen](http://doxygen.nl/)
  `@file` directive matches the actual name of the file it's in.
* `linelength_linter.py` - Ensure that code lines are <= 132 characters, block
  comments in code are <= 80 characters, and text lines are <= 80 characters.
  Lines that are long because of URLs are allowed. Only `http:`, `https:`, and
  `mailto:` URLs are considered URLs. Also, only C block comments are
  supported.
* `todo_linter.py` - Ensure that all "TODO" comments are accompanied by a
  Phabricator Task ID.

You can disable the TODO linter's complaints for a particular file by including
a line with:

```
@todo_linter: disable
```

It uses that syntax because we're using
[Doxygen](http://doxygen.nl/) for our API docs. Also, that
only exists so the linter won't complain when it's linting itself. `;-)`

### System Requirements

* Python 3.x

If you're calling these from the
[Arcanist](https://secure.phabricator.com/book/phabricator/article/arcanist/)
tool (used with
[Phabricator](https://secure.phabricator.com/book/phabricator/)), our
`.arclint` config for the linters looks like this:

```
{
    "linters": {
        "line_length_code": {
            "type": "script-and-regex",
            "script-and-regex.script": "./tools/linelength_linter.py --code",
            "script-and-regex.regex": "/^(?P<severity>Warning): (?P<line>\\d+): (?P<message>.*)$/m",
            "include": [
                "(.*\\.c$)",
                "(.*\\.h$)",
                "(.*\\.py$)"
            ]
        },
        "line_length_text": {
            "type": "script-and-regex",
            "script-and-regex.script": "./tools/linelength_linter.py --text",
            "script-and-regex.regex": "/^(?P<severity>Warning): (?P<line>\\d+): (?P<message>.*)$/m",
            "include": [
                "(.*\\.md$)",
                "(.*\\.txt$)"
            ]
        },
        "doxygen_file": {
            "type": "script-and-regex",
            "script-and-regex.script": "./tools/doxygen_file_linter.py",
            "script-and-regex.regex": "/^(?P<severity>Warning): (?P<line>\\d+): (?P<message>.*)$/m",
            "include": [
                "(.*\\.c$)",
                "(.*\\.h$)"
            ]
        },
        "todo_check": {
            "type": "script-and-regex",
            "script-and-regex.script": "./tools/todo_linter.py",
            "script-and-regex.regex": "/^(?P<severity>Warning): (?P<line>\\d+): (?P<message>.*)$/m",
            "include": [
                "(.*\\.h)",
                "(.*\\.c)",
                "(.*\\.py)",
                "(.*\\.txt)"
            ]
        },
        "copyright_check": {
            "type": "script-and-regex",
            "script-and-regex.script": "./tools/copyright_linter.py",
            "script-and-regex.regex": "/^(?P<severity>Warning): (?P<line>\\d+): (?P<message>.*)$/m",
            "include": [
                "(.*\\.h)",
                "(.*\\.c)",
                "(.*\\.py)"
            ],
            "exclude": [
                "(3rdparty/.*$)"
            ]
        }
    }
}
```

That checks line lengths on `.c`, `.h`, `.py`, `.md`, and `.txt` files, and
checks for valid TODO items on `.c`, `.h`, `.py`, and `.txt` files. The `.c`
and `.h` files also have their Doxygen `@file` directives checked.

## License

See the `LICENSE` file for details:

> Copyright 2016-2020 ISARA Corporation
>
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
>
> http://www.apache.org/licenses/LICENSE-2.0
>
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.
