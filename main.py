from window import Window
from draw import Point, Line, Cell, Maze

win = Window(800, 600)
maze = Maze(2, 2, 20, 20, 20, 20, win)
maze._create_cells()
maze._break_entrance_and_exit()
win.wait_for_close()