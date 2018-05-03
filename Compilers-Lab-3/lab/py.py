import sys

li = []
pos = None
plus_ = ["plus", "minus"]
times_ = ["times", "divide"]


def error(p, errMsg):
    print("ERROR AT LINE", p + 1)
    print(errMsg)
    sys.exit(-1)


def checkRange(errMsg=None):
    if pos >= len(li):
        error(pos, errMsg)


def parseExpression():
    global pos
    checkRange("不完整的表达式")
    if li[pos][0] in plus_:
        pos += 1
    parseTerm()
    while pos < len(li) and li[pos][0] in plus_:
        pos += 1
        parseTerm()


def parseTerm():
    global pos
    parseFactor()

    while pos < len(li) and li[pos][0] in times_:
        pos += 1
        parseFactor()


def parseFactor():
    global pos
    checkRange("缺少因子")
    if li[pos][0] in ["ident", "number"]:
        pos += 1
    else:
        if li[pos][0] == "lparen":
            pos += 1
        else:
            error(pos, "因子必须是符号，数字或者是由括号包裹的表达式")
        parseExpression()
        checkRange("括号不匹配")
        if li[pos][0] == "rparen":
            pos += 1
        else:
            error(pos, "括号不匹配")


if __name__ == "__main__":
    loop = int(input())
    for _ in range(loop):
        li.append([e.strip() for e in input().strip()[1:-1].split(",")])
    li = [str.lower(each) for each in li]
    print(li)
    pos = 0
    parseExpression()
    if pos > len(li):
        error(pos, "多余的符号")
    elif pos < len(li):
        error(pos, "未知的错误")
    print("OJBK")
