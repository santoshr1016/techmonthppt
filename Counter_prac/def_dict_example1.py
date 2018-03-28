import collections

#normal dictionary
# normal_dict = dict()
# normal_dict['k1'] = 'v1'
# normal_dict['k2'] = 'v2'
# print(normal_dict)
# print(normal_dict['k3'])

# Be sure to pass the function object to defaultdict().
def my_factory():
    return "default value"

def_dict = collections.defaultdict(my_factory)
def_dict['key1'] = "val1"
def_dict['key2'] = "val2"
def_dict['key3'] = "val3"

print(def_dict)
print(def_dict['key11'])

# default dict with list as default
def_dict_list = collections.defaultdict(list)
def_dict_list['python'].append("awesome")
def_dict_list['something-else'].append("not relevant")
def_dict_list['python'].append("language")
for i in def_dict_list.items():
    print(i)

# using lambda
def_dict_lambda = collections.defaultdict(lambda: "default val")
def_dict_lambda['hello'] = "world"
def_dict_lambda['python'] = "lang"
print(def_dict_lambda)
print(def_dict_lambda['accion'])