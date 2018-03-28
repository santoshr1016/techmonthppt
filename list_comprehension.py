l = [i*2 for i in range(10)]
print(l)

regular_dict = dict()
regular_dict['a'] = "val1"
regular_dict['b'] = "val2"
regular_dict['c'] = "val3"
regular_dict['d'] = "val4"
for v in regular_dict.values():
    print(v)


import collections
ordered_dict = collections.OrderedDict()
ordered_dict['a'] = "val1"
ordered_dict['b'] = "val2"
ordered_dict['c'] = "val3"
ordered_dict['d'] = "val4"
for v in ordered_dict.values():
    print(v)





