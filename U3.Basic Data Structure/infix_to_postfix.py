from pythonds3.basic import Stack
import string

def infix_to_postfix(infix_expr):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    op_stack=Stack()
    postfix_list=[]
    token_list=infix_expr.split()

    for i in range(len(token_list)):#修改算法以使其能处理输入异常情况
        if token_list[i] in string.ascii_uppercase and (
                token_list[i + 1] in string.ascii_uppercase or token_list[i - 1] == ")" or token_list[i + 1] == "("):
            return "Input Error"
        if token_list[i] in "+-*/" and (token_list[i + 1] in "+-*/)" or token_list[i - 1] in "+-*/("):
            return "Input Error"
        if i + 1 < len(token_list) and token_list[i] == ')' and token_list[i + 1] == "(":
            return "Input Error"


    for token in token_list:
        if token in "QWERTYUIOPASDFGHJKLZXCVBNM1234567890":postfix_list.append(token)
        elif token=='(':op_stack.push(token)
        elif token==')':
            top_token=op_stack.pop()
            while top_token!='(':
                postfix_list.append(top_token)
                top_token=op_stack.pop()
        else:
            while (not op_stack.is_empty())and(prec[op_stack.peek()]>=prec[token]):postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():postfix_list.append(op_stack.pop())
    return "".join(postfix_list)

print(infix_to_postfix("1 + 2 * 3 + 4"))#必须输入用空格分开的表达式，因为split方法按照空格分词