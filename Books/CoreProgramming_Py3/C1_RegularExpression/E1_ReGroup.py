import re


match = re.match('foo', 'foo')
print(match.group())
print(match.group(0))