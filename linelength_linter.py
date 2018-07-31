#!/usr/bin/env python3
'''
@file linelength_linter.py

@brief ISARA Radiate Security Suite toolkit's line length linter.

Code lines must be <= 132 characters, except block comments must be <= 80
characters. Text lines must be <= 80 characters. If there's a URL on the line,
the length is ignored, because some URLs are just too dang long.

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

URL_PATTERN = re.compile('^.*(http|https|mailto):.*$')  # Find a common URL.

COMMENT_LENGTH = 80  # Max line length for block comments or text files.
CODE_LENGTH = 132  # Max line length for code.


def check_text_lengths(lines):
    ''' Check the source lines for invalid line lengths.

    Output is "Warning: {lineno}: Line too long ({length}/{maxlength})"
    for each offending line.
    '''
    line_count = 1

    for line in lines:
        line = line.rstrip()  # This will let evil end-of-line whitespace people get away with it!

        if len(line) > COMMENT_LENGTH and not URL_PATTERN.match(line):
            print('Warning: {0}: Line too long ({1}/{2})'.format(line_count, len(line), COMMENT_LENGTH))
        line_count += 1


def check_code_lengths(lines):
    ''' Check the source lines for invalid line lengths.

    This is a bit more complicated because we have to know when we're inside a
    block comment.

    Output is "Warning: {lineno}: Line too long ({length}/{maxlength})"
    for each offending line.
    '''
    line_count = 1
    max_length = CODE_LENGTH

    for line in lines:
        # This isn't terribly robust. If you nest comments, it'll get confused.
        if '/*' in line and '*/' not in line:
            max_length = COMMENT_LENGTH

        if '*/' in line and '/*' not in line:
            max_length = CODE_LENGTH

        line = line.rstrip()  # This will let evil end-of-line whitespace people get away with it!

        if len(line) > max_length and not URL_PATTERN.match(line):
            print('Warning: {0}: Line too long ({1}/{2})'.format(line_count, len(line), max_length))
        line_count += 1


def main():
    ''' Look for lines that aren't following our line length conventions.
    '''
    for filename in sys.argv[1:]:
        if '--code' in filename or '--text' in filename:
            # Skip over argument.
            continue

        lines = None
        with open(filename) as file:
            lines = file.readlines()

        if '--code' in sys.argv:
            check_code_lengths(lines)
        elif '--text' in sys.argv:
            check_text_lengths(lines)
        else:
            raise SystemExit('You must specify --code or --text.')


if __name__ == '__main__':
    main()
