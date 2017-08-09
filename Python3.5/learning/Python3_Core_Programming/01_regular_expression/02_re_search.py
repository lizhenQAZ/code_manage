import re

try:
    match = re.match('foo', 'seafood')
    print(match.group())
except Exception as e:
    print('%s...' % e)
search = re.search('foo', 'seafood')
print(search.group())