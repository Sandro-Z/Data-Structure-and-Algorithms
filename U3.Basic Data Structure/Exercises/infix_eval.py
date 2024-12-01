"""这个程序是错误的，不能正确计算无任何括号的中序表达式"""
from pythonds3.basic import Stack

def infixEval(infixExpr):
    opstack = Stack()
    numstack = Stack()

    tokenList = infixExpr.split()

    for token in tokenList:
        if token in "+-*/()":
            if token == ")":
                while opstack.peek() != '(':
                    num2 = numstack.pop()
                    num1 = numstack.pop()
                    op = opstack.pop()
                    res = doMath(op, num1, num2)
                    numstack.push(res)
                opstack.pop()
            else:
                opstack.push(token)
        else:
            numstack.push(float(token))

    return numstack.pop()

def doMath(op, n1, n2):

    if op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    elif op == "+":
        return n1 + n2
    else:
        return n1 - n2

if __name__ == '__main__':
    print(infixEval("2 + 3 * 4"))
