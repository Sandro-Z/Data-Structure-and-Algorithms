import turtle


def draw_spiral(line_len):
    if line_len>0:
        turtle.forward(line_len)
        turtle.right(90)
        draw_spiral(line_len-5)

if __name__=='__main__':
    draw_spiral(100)
    turtle.done()