from stackClass import Stack

values = Stack()
for i in range(10):
    if i % 3 == 0:
        values.push(i)
    elif i % 4 == 0:
        values.pop()
        
print(values)