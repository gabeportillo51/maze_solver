from window import Window
from draw import Point, Line, Cell, Maze

win = Window(800, 600)
maze = Maze(2, 2, 30, 30, 20, 20, win, 0)
maze._create_cells()
maze._break_entrance_and_exit()
maze._break_walls_r(0, 0)
maze._reset_cells_visited()
win.wait_for_close()