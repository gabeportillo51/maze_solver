from window import Window
from draw import Point, Line, Cell, Maze

win = Window(800, 600)
maze = Maze(2, 2, 20, 20, 50, 50, win)
maze._create_cells
win.wait_for_close()