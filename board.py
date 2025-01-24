import random

START = "S"
END = "E"
WALL = "#"
SPACE = " "

class Board:
    """Maze. Has generation algorithms as methods."""
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.reset()

    def __str__(self):
        result = f"{''.join(('-' for c in range(self.width)))}\n"
        for row in self.board:
            result += f"{''.join((block for block in row))}|\n"
        result += f"{''.join(('-' for c in range(self.width)))}\n"
        return result

    def __iter__(self):
        return self.board.__iter__()

    def reset(self):
        """Resets board. Makes all blocks WALL."""
        self.board = [[WALL for x in range(self.width)] for y in range(self.height)]

    def binary_tree(self):
        """Generates maze using binary tree algorithm.
        returns all space cells in order for animation."""
        self.reset()
        result = []
        #returns all connections for animation.

        self.board[0] = [SPACE for ci in range(self.width)]
        result += [(0, ri) for ri in range(self.width)]
        #Must start with empty top.
        for ri, row in enumerate(self.board):
            row[0] = SPACE
            result.append((ri, 0))
        # Must start with empty left side.

        for ri in range(2, self.width, 2):
            for ci in range(2, self.height, 2):
                self.board[ri][ci] = SPACE
                result.append((ri, ci))
                #each (even, even) cell is a maze's path cell.
                conn = random.choice("nw")
                if conn == "n":
                    self.board[ri - 1][ci] = SPACE
                    result.append((ri - 1, ci))
                else:
                    self.board[ri][ci - 1] = SPACE
                    result.append((ri, ci - 1))
                #for each (even, even) cell, it randomly "connects" a corridor
                #to the cell at its north or west.
        return result


