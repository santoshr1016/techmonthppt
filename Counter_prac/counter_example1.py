from collections import Counter as ctr

print("Initial Counter")
print(ctr())
counter = ctr([(1,2), (1,1), (1,2), (2,1)])
print(counter)
print("*"*10)

# Modifying the counter
counter.update("abbefg")
print(counter)
print("*"*10)

# Modifying the counter using the dictionary
counter.update({'z':3, 'q':4})
print(counter)
print("*"*10)

# Getting the most repeated item
print(counter.most_common())
print(counter.most_common(3))
print("*"*10)

#iterating the counter
for letter in "abcd":
    print("{}, {}".format(letter, counter[letter]))

# Counter instances support arithmetic and set operations for aggregating results.
c1 = ctr(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = ctr('alphabet')
print(c1)
print(c2)

print("Combined counter", c1 + c2)
print("Subtract counter", c1 - c2)
print("Intersection counter", c1 & c2)
print("Union counter", c1 | c2)

