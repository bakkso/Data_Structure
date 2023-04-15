from stackClass import Stack

def checkBrackets(lines):
    s = Stack()
    for line in lines:
        for ch in line:
            if ch in ('{', '[', '('):
                s.push(ch)
            elif ch in ('}',']',')'):
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == ")" and left != "("):
                        return False
        if s.isEmpty() == False:
            return False
    return s.isEmpty()



filename = input("소스코드를 입력하세요 : ")
infile = open(filename, "r")
lines = infile.readlines()


print("filename --->", checkBrackets(lines))

infile.close()