from stackClass import Stack

import re

s = Stack()  # Stack 클래스의 인스턴스 생성

instr = input("문자열 입력: ")

instr = re.sub(r"[^a-zA-Z]", "", instr).lower()

sentence = instr[::-1]
"""
print(sentence)
print(instr)
"""
# instr[::-1]은 instr 문자열을 역순으로 정렬한 새로운 문자열을 만듦.
for sentence in instr[::-1]:  # instr 문자열을 역순으로 반복하며, 각 문자를 sentence 변수에 차례대로 저장
    s.push(sentence)
    # print(instr)

for sentence in instr[::-1]:
    if sentence != s.pop():
        print("회문이 아님")
        break
else:
    print("회문이 맞음")
