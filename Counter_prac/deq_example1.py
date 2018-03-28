from collections import deque

deq = deque([1,2,3,4,5])
print(deq)
deq.extend([11,22])

print(deq)
print("left end", deq[0])
print("right end", deq[-1])
deq.appendleft(111)
deq.append(999)
print(deq)
print(deq.pop())
print(deq.popleft())
deq.rotate(-2)
print(deq)
