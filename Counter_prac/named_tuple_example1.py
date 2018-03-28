from collections import namedtuple
lang = namedtuple("lang", "name author year")

result1 = lang("Python", "XYZ", 1995)
print(result1.name)
print(result1.author)
print(result1.year)

result2 = lang("C++", "BS", 1990)

for l in [result1, result2]:
    print(l.name, l.year, l.author)

