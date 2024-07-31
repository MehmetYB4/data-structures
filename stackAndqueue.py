#yığın yapısı
stack = [1,2,3]
stack.append(55)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


l2=[44,55,66] #illa liste olsun diyenler queue için
l2.append(77)
#l2.popleft()
l2.pop(0)
print(l2)


from collections import deque
#kuyruk yapısı
queue_=deque([11,22,45,78])
print(queue_)
print(queue_.popleft())
print(queue_)