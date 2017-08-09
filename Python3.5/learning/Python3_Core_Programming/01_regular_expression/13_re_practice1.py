import re


string = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
for i, element in enumerate(string):
    ret = re.match(r'b.t|h.t', element)
    print(i+1, '-', ret.group())