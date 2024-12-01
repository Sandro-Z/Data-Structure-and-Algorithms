import turtle as t

def draw_triangle(points,color):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def mid(p1,p2):return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski(points,degree):
    colormap=['blue','red','green','white','yellow','violet','orange']
    draw_triangle(points,colormap[degree])
    if degree>0:
        sierpinski([points[0],mid(points[0],points[1]),mid(points[0],points[2])],degree-1)
        sierpinski([points[1], mid(points[0], points[1]), mid(points[1], points[2])], degree - 1)
        sierpinski([points[2], mid(points[2], points[1]), mid(points[0], points[2])], degree - 1)

if __name__=='__main__':
    t.speed(9999)
    points=[[-100,-50],[0,100],[100,-50]]
    sierpinski(points,5)
    t.done()