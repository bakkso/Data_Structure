from stackClass import Stack

import re

s = Stack() #Stack 클래스의 인스턴스 생성

instr = input("문자열 입력: ")

instr = re.sub(r"[^a-zA-Z]", "", instr).lower()

sentence = instr[::-1]

print(sentence)
print(instr)

for sentence in instr[::-1]: 
    s.push(sentence)

for sentence in instr[::-1]:
    if sentence != s.pop():
        print("회문이 아님")
        break
else: 
    print("회문이 맞음")
   
