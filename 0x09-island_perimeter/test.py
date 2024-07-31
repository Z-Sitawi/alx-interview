import unittest
island_perimeter = __import__('0-island_perimeter').island_perimeter


class TestIslandPerimeter(unittest.TestCase):
    def test_single_cell_island(self):
        grid = [[1]]
        self.assertEqual(island_perimeter(grid), 4)

    def test_small_island_no_surrounding(self):
        grid = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(island_perimeter(grid), 8)

    def test_single_row_island(self):
        grid = [
            [1, 1, 1]
        ]
        self.assertEqual(island_perimeter(grid), 8)

    def test_single_column_island(self):
        grid = [
            [1],
            [1],
            [1]
        ]
        self.assertEqual(island_perimeter(grid), 8)

    def test_non_rectangular_island(self):
        grid = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
        self.assertEqual(island_perimeter(grid), 12)

    def test_island_with_holes(self):
        grid = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]
        ]
        self.assertEqual(island_perimeter(grid), 16)

    def test_no_island(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(island_perimeter(grid), 0)

    def test_complex_island_shape(self):
        grid = [
            [0, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 0]
        ]
        self.assertEqual(island_perimeter(grid), 18)

    def test_minimal_rectangular_island(self):
        grid = [
            [1, 1, 1]
        ]
        self.assertEqual(island_perimeter(grid), 8)

    def test_minimal_rectangular_island_vertical(self):
        grid = [
            [1],
            [1],
            [1]
        ]
        self.assertEqual(island_perimeter(grid), 8)

    def test_large_island(self):
        grid = [[0] * 100 for _ in range(100)]
        for i in range(1, 99):
            for j in range(1, 99):
                grid[i][j] = 1
        self.assertEqual(island_perimeter(grid), 392)


if __name__ == '__main__':
    unittest.main()
