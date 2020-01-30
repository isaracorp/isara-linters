#!/usr/bin/env python3
'''
@file doxygen_file_linter.py

@brief ISARA Radiate Security Suite toolkit's Doxygen @file linter.

For .h and .c files, we want a Doxygen @file directive at the top that
indicates the file name. This is slightly superstitious on our part, but it
does frequently warn us when we've copy/pasted a file and not updated its
comments. The linter is required because we keep forgetting to update the
@file directive, and we've started missing them in code reviews.

@copyright Copyright (C) 2019-2020, ISARA Corporation, All Rights Reserved.

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

import os.path
import re
import sys

DOXYGEN_FILE_PATTERN = re.compile(r'^(/\*\*|//) @file (?P<filename>[^\s]+).*$')


def check_doxygen_file(filename, lines):
    ''' Check for a proper @file directive.

    Output is "Warning: {lineno} Invalid @file: {line}" for each invalid @file
    or "Warning: 1 Missing @file" if no @file directive is present.
    '''
    line_count = 1
    found_directive = False
    for line in lines:
        directive = DOXYGEN_FILE_PATTERN.match(line)
        if directive:
            found_directive = True

            if directive.group('filename') != filename:
                print('Warning: {0} Invalid @file: {1}'.format(line_count, line.strip()))

            break

        line_count += 1

    if not found_directive:
        print('Warning: 1 Missing @file directive')


def main():
    ''' Look for files that don't have a proper @file directive.
    '''
    for filename in sys.argv[1:]:
        lines = None
        with open(filename) as file:
            lines = file.readlines()

        base_filename = os.path.basename(filename)

        check_doxygen_file(base_filename, lines)


if __name__ == '__main__':
    main()
