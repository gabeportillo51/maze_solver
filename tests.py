import unittest
from draw import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_entrance_exit(self):
        m1 = Maze(0, 0, 12, 10, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].top_wall, False)
        self.assertEqual(m1._cells[9][11].right_wall, False)

if __name__ == "__main__":
    unittest.main()