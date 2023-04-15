from stackClass import Stack

s1 = Stack()
s2 = Stack()

# P_5.2


def QueueUsingStack_push(item):
    #item = input()
    # #호출될 때 인자로 item을 넘기지 않고 input()을 호출하고 있습니다.
    # 이 경우 함수 호출 시 입력을 받을 수 있지만,
    # 함수가 호출되는 동안 프로그램이 멈추고 입력을 기다리는 문제가 발생
    s1.push(item)


def QueueUsingStack_pop():
    if s2.isEmpty():
        while not s1.isEmpty():
            s2.push(s1.pop())
    return s2.pop()


QueueUsingStack_push(1)
QueueUsingStack_push(3)
QueueUsingStack_push(7)


print(QueueUsingStack_pop())
print(QueueUsingStack_pop())
print(QueueUsingStack_pop())
