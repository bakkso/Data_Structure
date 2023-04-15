from stackClass import Stack
from evalPrefix import evalPrefix

expr = input("입력 수식(공백문자로 분리): ")
prefix = expr.split(' ')

print(' 전위표기: ', prefix)

#prefix.reverse()
result = evalPrefix(prefix)
print(' 계산결과: ', result)
