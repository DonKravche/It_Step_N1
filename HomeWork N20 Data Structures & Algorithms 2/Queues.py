
#################################################
# deque
#################################################

import collections

deq = collections.deque([1, 6, 33, 10, 15, 10, 25, 23])
deq.append(100)
deq.appendleft(200)
print(deq.index(10))
print(deq.count(10))
deq.insert(2, 1000)
print(deq)
print(deq.pop())
print(deq)
print(deq.popleft())
print(deq)

#################################################
# Queue
#################################################

from queue import Queue

q = Queue(maxsize=4)
print(q.qsize())

q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put_nowait('d')
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
# print(q.get_nowait())
print(q.qsize())
