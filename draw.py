class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, canvas):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = canvas
        self.top_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.right_wall = True

    def draw(self, point_1, point_2):
        self._x1 = point_1.x
        self._y1 = point_1.y
        self._x2 = point_2.x
        self._y2 = point_2.y
        if self.top_wall == True:
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(self._win, "black")
        if self.bottom_wall == True:
            Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(self._win, "black")
        if self.left_wall == True:
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(self._win, "black")
        if self.right_wall == True:
            Line(Point(self._x2, self._y2), Point(self._x2, self._y1)).draw(self._win, "black")