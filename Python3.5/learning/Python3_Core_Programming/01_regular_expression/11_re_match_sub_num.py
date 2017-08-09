import re


m = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2,5})', r'\3/\1/\2', '2/20/2017')
print(m)