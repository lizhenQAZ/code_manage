# coding: utf-8
import unicodedata
import re
re_digit = re.compile(r'\d')
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
for char in sample:
    print('U+%04x' % ord(char), char.center(6), 're_dig' if re_digit.match(char) else '-'.center(6),
          'isdig' if char.isdigit() else '-'.center(6),
          'isnum' if char.isnumeric() else '-'.center(6),
          format(unicodedata.numeric(char), '5.2f'),
          unicodedata.name(char), sep='\t')
