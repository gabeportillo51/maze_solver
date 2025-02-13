import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            self.seed = random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cells.append([Cell(self.win) for i in range(self.num_rows)])
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
        
        
    def _draw_cell(self, i, j):
        moving_x = self.x1 + (i*self.cell_size_x)
        moving_y = self.y1 + (j*self.cell_size_y)
        upper_left = Point(moving_x, moving_y)
        lower_right = Point(moving_x + self.cell_size_x, moving_y + self.cell_size_y)
        self._cells[i][j].draw(upper_left, lower_right)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].right_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i-1 >= 0:
                if self._cells[i-1][j].visited == False:
                    to_visit.append((i-1, j))
            if i + 1 <= self.num_cols - 1:
                if self._cells[i+1][j].visited == False:
                    to_visit.append((i+1, j))
            if j-1 >= 0:
                if self._cells[i][j-1].visited == False:
                    to_visit.append((i, j-1))
            if j + 1 <= self.num_rows - 1:
                if self._cells[i][j+1].visited == False:
                    to_visit.append((i, j+1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            rand_next = random.randrange(0, len(to_visit))
            next = to_visit[rand_next]
            to_visit.clear()
            if next[0] < i:
                self._cells[i][j].left_wall = False
                self._cells[next[0]][j].right_wall = False
            if next[0] > i:
                self._cells[i][j].right_wall = False
                self._cells[next[0]][j].left_wall = False
            if next[1] < j:
                self._cells[i][j].top_wall = False
                self._cells[i][next[1]].bottom_wall = False
            if next[1] > j:
                self._cells[i][j].bottom_wall = False
                self._cells[i][next[1]].top_wall = False
            self._break_walls_r(next[0], next[1])
        
    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        end = self._cells[self.num_cols-1][self.num_rows-1]
        if self._cells[i][j] == end:
            return True
        if (i-1 >= 0) and (self._cells[i][j].left_wall == False) and (self._cells[i-1][j].visited == False):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)

        if (j-1 >= 0) and (self._cells[i][j].top_wall == False) and (self._cells[i][j-1].visited == False):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)

        if (i+1 <= self.num_cols-1) and (self._cells[i][j].right_wall == False) and (self._cells[i+1][j].visited == False):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)

        if (j+1 <= self.num_rows-1) and (self._cells[i][j].bottom_wall == False) and (self._cells[i][j+1].visited == False):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        return False







class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, win, fill_color):
        win.canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.top_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.right_wall = True
        self.visited = False

    def draw(self, point_1, point_2):
        self._x1 = point_1.x
        self._y1 = point_1.y
        self._x2 = point_2.x
        self._y2 = point_2.y
        if self.top_wall == True:
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(self._win, "black")
        if self.top_wall == False:
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(self._win, "#d9d9d9")
        if self.bottom_wall == True:
            Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(self._win, "black")
        if self.bottom_wall == False:
            Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(self._win, "#d9d9d9")
        if self.left_wall == True:
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(self._win, "black")
        if self.left_wall == False:
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(self._win, "#d9d9d9")
        if self.right_wall == True:
            Line(Point(self._x2, self._y2), Point(self._x2, self._y1)).draw(self._win, "black")
        if self.right_wall == False:
            Line(Point(self._x2, self._y2), Point(self._x2, self._y1)).draw(self._win, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        center_self_x = ((self._x2 - self._x1) / 2) + self._x1
        center_self_y = ((self._y2 - self._y1) / 2) + self._y1
        center_of_self = Point(center_self_x, center_self_y)
        center_to_x = ((to_cell._x2 - to_cell._x1) / 2) + to_cell._x1
        center_to_y = ((to_cell._y2 - to_cell._y1) / 2) + to_cell._y1
        center_of_to = Point(center_to_x, center_to_y)
        if undo == False:
            Line(center_of_self, center_of_to).draw(self._win, "red")
        if undo == True:
            Line(center_of_self, center_of_to).draw(self._win, "gray")

