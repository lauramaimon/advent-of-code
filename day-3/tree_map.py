
class TreeMap:
    def __init__(self, grid, width, height):
        self.grid = grid
        self.width = width
        self.height = height

    @classmethod
    def from_file(cls, filepath: str):
        # assumes input file is correctly formatted:
        # - has at least one row
        # - every row is the same length
        with open(filepath) as f:
            rows = [line.strip() for line in f]
        width = len(rows[0])
        height = len(rows)
        return cls(rows, width, height)


    def is_tree(self, x: int, y: int):
        if not self.is_within_map:
            return False
        return self.grid[y][x % self.width] == "#"


    def is_within_map(self, y: int):
        return 0 <= y < self.height
