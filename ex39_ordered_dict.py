import collections
d = collections.OrderedDict()
d[3] = 'A'
d[2] = 'B'
d[1] = 'C'


for k, v in d.items():
    print k, v

print '-' * 10	
dict = {3:'A', 2:'B', 1:'C'}
for k, v in dict.items():
    print k, v 