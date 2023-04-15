from stackClass import Stack
from evalPostfix import evalPostfix
from Infix2Posfix import Infix2Postfix

expr = input("입력 수식(공백문자로 분리): ")
infix = expr.split(" ")
    
print(' 중위표기: ',infix)

postfix = Infix2Postfix(infix)
print(' 후위표기: ',postfix)

result = evalPostfix(postfix)
print(' 계산결과 : ',result)