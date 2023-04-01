def delete(pos):
    return list.pop(pos)

def replace(pos, elem):
    list[pos] = elem

def size():
    return len(list)

def display(msg='ArrayList:'):
    print(msg, size(), list)

list = []

list.insert(0, 10)
display()
list.insert(1, 20)
display()
list.insert(0, 30)
display()
list.insert(2, 40)
display()
list.insert(size(), 50)
display()
list.insert(1, 60)
display()
replace(2, 70)
display()
delete(2)
display()
