import re

# A -> BF
# F -> +A | -A | ε
# B -> CG
# G -> *B | \B | ε
# C -> DE
# E -> ^C | ε
# D -> (A) | i

li = []
curIndex = 0
tmp = 0

def parseA():
    resultB, varB = parseB()
    charF, resultF, varF = parseF()
    if charF == "+":
        t = getTmpVar()
        print("(+, " + varB + ", " + varF + ", " + t + ")")
        return resultB + resultF, t
    elif charF == "-":
        t = getTmpVar()
        print("(-, " + varB + ", " + varF + ", " + t + ")")
        return resultB - resultF
    elif charF is None:
        return resultB, varB
    else:
        raise Exception("error")


def parseF():
    if peekNext() == "+":
        ch = getNext()
        rA, vA = parseA()
        return ch, rA, vA
    elif peekNext() == "-":
        ch = getNext()
        rA, vA = parseA()
        return ch, rA, vA
    else:
        return None, None, None


def parseB():
    resultC, varC = parseC()
    charG, resultG, varG = parseG()
    if charG == "*":
        t = getTmpVar()
        print("(*, " + varC + ", " + varG + ", " + t + ")")
        return resultC * resultG, t
    elif charG == "/":
        t = getTmpVar()
        print("(/, " + varC + ", " + varG + ", " + t + ")")
        return resultC / resultG, t
    elif charG is None:
        return resultC, varC
    else:
        raise Exception("error")


def parseG():
    if peekNext() == "*":
        ch = getNext()
        rB, vB = parseB()
        return ch, rB, vB
    elif peekNext() == "/":
        ch = getNext()
        rB, vB = parseB()
        return ch, rB, vB
    else:
        return None, None, None


def parseC():
    resultD, varD = parseD()
    charE, resultE, varE = parseE()
    if charE == "^":
        t = getTmpVar()
        print("(^, " + varD + ", " + varE + ", " + t + ")")
        return resultD ** resultE, t
    elif charE is None:
        return resultD, varD
    else:
        raise Exception("error")


def parseE():
    if peekNext() == "^":
        ch = getNext()
        rC, vC = parseC()
        return ch, rC, vC
    else:
        return None, None, None

def parseD():
    if peekNext() == "(":
        getNext()
        ret, varA = parseA()
        if getNext() != ")":
            raise Exception("error")
        return ret, varA
    elif isNum(peekNext()):
        n = getNext()
        return int(n), str(n)
    else:
        raise Exception("error")



def peekNext():
    global curIndex
    if curIndex < len(li):
        return li[curIndex]
    else:
        return None


def getNext():
    global curIndex
    if curIndex < len(li):
        ret = li[curIndex]
        curIndex += 1
        return ret
    else:
        return None

def isNum(str):
    result = re.match('''^\d+$''', str)
    if result is not None:
        return True
    else:
         return False


def getTmpVar():
    global tmp
    ret = "t" + str(tmp)
    tmp += 1
    return ret




if __name__=="__main__":
    print("INPUT EXPRESSION OR 'exit' TO EXIT")
    print("SUPPORT: (\d+|[()^+\-*/])+")
    pattern = re.compile('''\d+|[()^+\-*/]''')
    while True:
        expr = input(">>>")
        tmp = 0
        curIndex = 0
        li = re.findall(pattern, expr)
        if expr == "exit":
            break
        if re.match('''(\d+|[()^+\-*/])+''', expr) is None:
            print("EXIST UNSUPPORTED CHARACTER(S)")
            continue
        print(li)
        try:
            result, var = parseA()
            print("RESULT VAR:", var)
            print("RESULT:", result)
        except Exception as e:
            print(e)

