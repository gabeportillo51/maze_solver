from window import Window
from draw import Point, Line, Cell

win = Window(800, 600)
first_cell = Cell(win.canvas)
second_cell = Cell(win.canvas)
third_cell = Cell(win.canvas)
fourth_cell = Cell(win.canvas)
fifth_cell = Cell(win.canvas)
first_cell.draw(Point(236, 10), Point(45, 471))
second_cell.draw(Point(18, 173), Point(66, 160))
third_cell.draw(Point(84, 212), Point(270, 270))
fourth_cell.draw(Point(342, 75), Point(360, 360))
fifth_cell.draw(Point(745, 323), Point(656, 156))
first_cell.draw_move(second_cell)
first_cell.draw_move(third_cell)
first_cell.draw_move(fourth_cell, undo=True)
first_cell.draw_move(fifth_cell)
win.wait_for_close()