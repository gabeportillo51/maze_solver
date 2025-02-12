from window import Window
from draw import Point, Line

win = Window(800, 600)
point_1 = Point(55, 200)
point_2 = Point(500, 13)
point_3 = Point(99, 450)
point_4 = Point(250, 350)
point_5 = Point(700, 100)
line_1 = Line(point_1, point_5)
line_2 = Line(point_2, point_4)
line_3 = Line(point_3, point_1)
win.draw_line(line_1, "black")
win.draw_line(line_2, "red")
win.draw_line(line_3, "green")
win.wait_for_close()