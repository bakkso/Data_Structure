from dequeue import Deque

import re

d = Deque()  # Deque 클래스의 인스턴스 생성

instr = input("문자열 입력: ")

instr = re.sub(r"[^a-zA-Z]", "", instr).lower()

sentence = instr[::-1]  # instr 문자열 회문을 판별하기 위해 역순으로 sentence에 삽입.


print("sentence : ", sentence)
print("instr : ", instr)

# instr[::-1]은 instr 문자열을 역순으로 정렬한 새로운 문자열을 만듦.
for sentence in instr[::-1]:  # instr 문자열을 역순으로 반복하며, 각 문자를 sentence 변수에 차례대로 저장
    d.addRear(sentence)  # 덱의 뒤에서부터 sentence변수를 차례대로 삽입
    d.display()

for sentence in instr[::-1]:
    # sentence, 즉 instr의 역순의 변수가 덱의 Rear와 같지않다면
    # -> 덱의 front가 아닌 rear인 이유 front를 하면 instr의 역순이 삽입된 현재 덱을 그대로 출력(삭제후 반환)해준 것이기떄문에
    # 현재 sentence는 instr의 역순의 변수임, 근데 덱 또한 위 for문에서 역순의 instr를 삽입했음
    # 이런 상황에서 덱의 deleteFront를 한다면 sentence도 순서대로 읽고 덱도 순서대로 읽은거니까 회문판별이 아님.
    # 즉, 역순 <-> 순 이 같으면 회문인데 front를 한다면 역순 <-> 역순 을 판별한 셈이 됨.
    if sentence != d.deleteRear():
        print("회문이 아님")
        break
else:
    print("회문이 맞음")
