from window import Window
from draw import Point, Line, Cell, Maze

win = Window(800, 600)
maze = Maze(2, 2, 25, 25, 15, 15, win, 0)
maze._create_cells()
maze._break_entrance_and_exit()
maze._break_walls_r(0, 0)
maze._reset_cells_visited()
maze.solve()
win.wait_for_close()