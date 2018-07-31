#!/usr/bin/env python3
'''
<!-- @todo_linter: disable -->
@file todo_linter.py

@brief ISARA Radiate Security Suite toolkit's TODO comment linter.

All TODO comments must be accompanied by a Task ID.

@copyright Copyright 2017-2018, ISARA Corporation, All Rights Reserved.

@license Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<a href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import re
import sys

TODO_PATTERN = re.compile('^.*(FIXME|TODO|XXX).*$', re.IGNORECASE)  # Find TODO lines.
VALID_TODO_PATTERN = re.compile('^.*(FIXME|TODO|XXX).*(T[0-9]+).*$')  # Is it a valid TODO line?
DISABLE_TODO_PATTERN = re.compile('^.*@todo_linter: disable.*$')  # Disable TODO linting on this file?


def check_todos(lines):
    ''' Check the source lines for invalid TODO comments.

    Output is "Warning: {lineno} Invalid TODO: {code}" for each invalid TODO.
    '''
    line_count = 1
    for line in lines:
        if DISABLE_TODO_PATTERN.match(line):
            # Don't do TODO linting on this set of lines.
            return

        if TODO_PATTERN.match(line) and not VALID_TODO_PATTERN.match(line):
            print('Warning: {0}: Invalid TODO, add Task reference.'.format(line_count))
        line_count += 1


def main():
    ''' Look for TODO/FIXME/XXX that don't have an associated Task ID.
    '''
    for filename in sys.argv[1:]:
        lines = None
        with open(filename) as file:
            lines = file.readlines()

        check_todos(lines)


if __name__ == '__main__':
    main()
