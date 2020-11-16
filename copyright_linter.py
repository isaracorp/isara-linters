#!/usr/bin/env python3
'''
@file copyright_linter.py

@brief ISARA Radiate Security Suite toolkit's Copyright comment linter.

All Copyright comments must have the correct year in them.

@copyright Copyright (C) 2017-2020, ISARA Corporation, All Rights Reserved.

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
import time

# Copyright statements are assumed to be using Doxygen format, such as:
#
# @copyright Copyright (C) 2017-2020, ISARA Corporation, All Rights Reserved.
COPYRIGHT_PATTERN = re.compile(r'^.*@copyright Copyright \(C\) (([0-9]{4})-)?([0-9]{4}), ISARA Corporation, All Rights Reserved.$')


def check_copyright(lines):
    ''' Check the source lines for missing or invalid Copyright comments.

    Output is "Warning: {lineno} Invalid Copyright statement."
    '''
    this_year = time.localtime().tm_year

    found_copyright = False
    line_count = 1
    for line in lines:
        match = COPYRIGHT_PATTERN.match(line)
        if match:
            found_copyright = True

            _, start_year, end_year = match.groups()
            if int(end_year) != this_year:
                print('Warning: {0}: Invalid Copyright year.'.format(line_count))

            if start_year and int(start_year) >= this_year:
                print('Warning: {0}: Invalid Copyright range.'.format(line_count))

        line_count += 1

    if not found_copyright:
        print('Warning: {0}: No Copyright found.'.format(line_count))


def main():
    ''' Look for invalid/out-of-date Copyright lines.
    '''
    for filename in sys.argv[1:]:
        lines = None
        with open(filename) as file:
            lines = file.readlines()

        check_copyright(lines)


if __name__ == '__main__':
    main()
