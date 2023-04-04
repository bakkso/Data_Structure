""""
from stackClass import Stack
from evalPostfix import evalPostfix #계산
from Infix2Posfix import Infix2Postfix #Infix2Posfix = 중위표기수식 -> 후위표기수식

while True:
    expr = input("입력 수식(공백문자로 분리): ")
    infix = expr.split(" ")
    for i in expr:
        if i not in '0123456789+-*/().':
            print("올바른 수식이 아닙니다. 다시 입력하세요.")
            continue
    print(' 중위표기: ',infix)

    postfix = Infix2Postfix(infix)
    print(' 후위표기: ',postfix)

    result = evalPostfix(postfix)
    print(' 계산결과 : ',result)
    """
    
from stackClass import Stack
from evalPostfix import evalPostfix
from Infix2Posfix import Infix2Postfix

while True:
    expr = input("입력 수식(공백문자로 분리): ")
    infix = expr.split(" ")
    
    for token in infix:
        try:
            float(token)  # 숫자인 경우 아무 작업도 하지 않음
        except ValueError:
            if token not in '+-*/()':
                print("올바른 수식이 아닙니다. 다시 입력하세요.")
                break
    else:
        print(' 중위표기: ',infix)

        postfix = Infix2Postfix(infix)
        print(' 후위표기: ',postfix)

        result = evalPostfix(postfix)
        print(' 계산결과 : ',result)
