from pythonds3 import Deque

def pal_checker(string):
    char_deque=Deque()
    for ch in string:
        if ch!=(" "):#根据习题要求，添加了去除空格的功能
            char_deque.add_rear(ch)
    while char_deque.size()>1:
        first=char_deque.remove_front()
        last=char_deque.remove_rear()
        if first!=last:return False
    return True

print(pal_checker("上海自来水 来自 海上"))