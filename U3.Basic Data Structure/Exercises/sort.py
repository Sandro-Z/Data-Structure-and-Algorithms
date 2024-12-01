from pythonds3.basic import Queue

"""这个程序的特点就是队列比较多，而且有嵌套，逻辑上一定要弄清楚"""
def cardinalitysorted(alist):
    result = []
    masterq = Queue()  #主桶
    numslist = []
    maxnumlen = 0
    for i in range(10):
        numslist.append(Queue())  #把10个桶队列加入到桶的列表中

    for i in range(len(alist)):
        maxnumlen = max(maxnumlen, len(str(alist[i])))  #检测最多有几位数字
        masterq.enqueue(alist[i])

    for i in range(maxnumlen):  #比较最多位数次
        while not masterq.is_empty():
            cur = masterq.dequeue()
            radix = int(cur / (10 ** i) % 10)#比较的那一位
            numslist[radix].enqueue(cur)
        for j in range(10):
            while not numslist[j].is_empty():
                masterq.enqueue(numslist[j].dequeue())

    for i in range(len(alist)):
        result.append(masterq.dequeue())

    return result


if __name__ == '__main__':
    ml = [54, 678, 3215, 57, 4123, 3, 3535, 90]
    print(cardinalitysorted(ml))
