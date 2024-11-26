#!/usr/bin/env python3

import argparse

#####################
## Set Up Argparse ##
#####################

# Initialize argparse
parser = argparse.ArgumentParser(
    description='Print any number of smiley emoticons on the same or a different line')

'''
# Required arguments
parser.add_argument('--num', required=True, type=int,
    metavar='<int>', help='Required integer argument to choose number of smiley emoticons to print')
'''

# Optional arguments
parser.add_argument('--num', required=False, type=int, default = 5,
    metavar='<int>', help='Integer argument to choose number of smiley emoticons to print, default is [%(default)i]')
    
# Switch
parser.add_argument('--same', action="store_true",
   help='If used, the smiley emoticon are printed on the same line instead of different lines')

# Finalization of argparse
arg = parser.parse_args()

if arg.same:
    a = ':) '
    b = a * arg.num
else:
    a = ':) \n'
    b = a * arg.num
print(b)