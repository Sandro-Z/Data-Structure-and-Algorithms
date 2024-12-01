import turtle as t
def tree(branch_len):
    if branch_len>5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-15)
        t.left(40)
        tree(branch_len-15)
        t.right(20)
        t.backward(branch_len)

if __name__=='__main__':
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color('green')
    tree(110)
    t.done()