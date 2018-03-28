from collections import Counter as ctr

with open("sample.txt") as f:
    counter = ctr()
    for line in f:
        counter.update(line.strip().split())
    print(counter.most_common())