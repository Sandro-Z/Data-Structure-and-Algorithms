#目前暂时无法正常运行
import turtle


Start='S'
obs='+'
tried='.'
dead_end='-'
part_of_path='0'

class Maze:
    def __init__(self,maze_filename):#构造函数
        with open(maze_filename,"r") as maze_file:
            self.maze_list=[
                [ch for ch in line.strip('\n')]
                for line in maze_file.readlines()
            ]#读入迷宫，并以列表的形式形成一个矩阵
        self.rows_in_maze=len(self.maze_list)
        self.columns_in_maze=len(self.maze_list[0])
        for row_idx,row in enumerate(self.maze_list):
            if Start in row:
                self.start_row=row_idx
                self.start_col=row.index(Start)
                break
        self.x_translate=-self.columns_in_maze/2
        self.y_translate=self.rows_in_maze/2
        self.t=turtle.Turtle()
        self.t.shape("turtle")
        self.wn=turtle.Screen()
        self.wn.setworldcoordinates(
            -(self.columns_in_maze-1)/2-0.5,
            -(self.rows_in_maze-1)/2-0.5,
            (self.columns_in_maze-1)/2+0.5,
            (self.rows_in_maze-1)/2+0.5)###

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x]==obs:
                   self.draw_centered_box(
                        x+self.x_translate,
                        -y+self.y_translate,
                        'orange'
                    )
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self,x,y,color):
        self.t.up()
        self.t.goto(x-0.5,y-0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def update_position(self,row,col,val=None):#移动方法
        if val:self.maze_list[row][col]=val
        self.move_turtle(col,row)

        if val==part_of_path:color='green'
        elif val==obs:color='red'
        elif val==tried:color='black'
        elif val==dead_end:color='red'
        else:color=None
        if color:self.drop_bread_crumb(color)

    def move_turtle(self,x,y):
        self.t.up()
        self.t.setheading(
            self.t.towards(
                x+self.x_translate
                -y+self.y_translate
            )
        )
        self.t.goto(x+self.x_translate,-y+self.y_translate)

    def drop_bread_crumb(self,color):
        self.t.dot(10,color)

    def is_exit(self,row,col):
        return(
            row in [0,self.rows_in_maze-1]
            or col in [0,self.columns_in_maze-1]
        )

    def __getitem__(self,idx):return self.maze_list[idx]

    def search_from(maze,row,column):
        maze.update_position(row,column)
        if maze[row][column]==obs:return False
        if maze[row][column] in [tried,dead_end]:return False
        if maze.is_exit(row,column):
            maze.update_position(row,column,part_of_path)
            return True
        maze.update_position(row,column,tried)
        found=(
            search_from(maze,row-1,column)
            or search_from(maze,row+1,column)
            or search_from(maze,row,column-1)
            or search_from(maze,row,column+1)
        )
        if found:maze.update_position(row,column,part_of_path)
        else:maze.update_position(row,column,dead_end)
        return found

if __name__=='__main__':
    m=Maze('maze')
    m.draw_maze()
    m.search_from(m,m.start_row,m.start_col)
