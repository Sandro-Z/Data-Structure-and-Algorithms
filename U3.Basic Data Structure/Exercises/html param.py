from pythonds3.basic import Stack

def parCheckerHtml(symbolString):
    s = Stack()
    matched = True
    index = 0
    while index < len(symbolString) and matched:
        str = symbolString[index]
        if str in ["<html>", "<head>", "<title>", "<body>","<h1>"]:
            s.push(str)
        if str in ["</html>", "</head>", "</title>", "</body>","</h1>"]:
            if s.is_empty():
                matched = False
            else:
                top = s.pop()
                if not matches(top, str):
                    matched = False

        index += 1

    if matched and s.is_empty():#只有在matched为假并且没有剩余的符号时才成功
        return True
    else:
        return False

def matches(left, right):
    lefts = ["<html>", "<head>", "<title>", "<body>","<h1>"]
    rights = ["</html>", "</head>", "</title>", "</body>","</h1>"]
    return lefts.index(left) == rights.index(right)

if __name__ == '__main__':

    file_path = "test.html"
    string = open(file_path).read().split()
    print(parCheckerHtml(string))
