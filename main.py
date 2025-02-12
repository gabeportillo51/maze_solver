from window import Window
from draw import Point, Line, Cell

win = Window(800, 600)
first_cell = Cell(win.canvas)
second_cell = Cell(win.canvas)
third_cell = Cell(win.canvas)
fourth_cell = Cell(win.canvas)
fifth_cell = Cell(win.canvas)
first_cell.draw(Point(10, 10), Point(90, 90))
second_cell.top_wall = False
second_cell.draw(Point(100, 100), Point(160, 160))
third_cell.bottom_wall = False
third_cell.draw(Point(200, 200), Point(270, 270))
fourth_cell.left_wall = False
fourth_cell.draw(Point(300, 300), Point(360, 360))
fifth_cell.right_wall = False
fifth_cell.draw(Point(450, 450), Point(550, 550))
win.wait_for_close()