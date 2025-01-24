"""Program that animates maze generation algorithms."""
import pygame
from board import *

class Window:
    """Manages pygame window. Can draw and animate maze generation."""
    def __init__(self, width, board_d, wall_color, bg):
        self.WIDTH = width
        self.board = Board(board_d[0], board_d[1])
        self.BLOCK_WIDTH = width // board_d[0]
        self.HEIGHT = self.BLOCK_WIDTH * board_d[1]
        self.WALL_COLOR = wall_color
        self.BG = bg

        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Maze Generation")
        self.clock = pygame.time.Clock()
        self.running = True

        self.past_frame_spacebar = False
        self.current_frame_spacebar = False

        while self.running:
            self.clock.tick(30)

            self.check_for_quit()
            self.check_for_spacebar()

            pygame.display.update()
        pygame.quit()

    def check_for_spacebar(self):
        """Checks if the spacebar was pressed to generate maze."""
        keys = pygame.key.get_pressed()
        self.past_frame_spacebar = self.current_frame_spacebar
        if keys[pygame.K_SPACE]:
            self.current_frame_spacebar = True
        else:
            self.current_frame_spacebar = False
        #simple frame-by-frame queue system from frame presses
        #to avoid repeating the algorithm when
        #the space bar is pressed for more than one frame.

        if self.past_frame_spacebar and not self.current_frame_spacebar:
            self.animate_maze()
            #generates the maze if it was pressed.

    def check_for_quit(self):
        """Checks if user has clicked on window's x and exits the program."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def animate_maze(self):
        """Animates maze generation algorithm in a nested window loop."""
        self.WINDOW.fill(self.WALL_COLOR)

        rects = self.board.binary_tree()
        for pos in rects:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            pygame.draw.rect(self.WINDOW,
                             self.BG,
                             pygame.Rect(pos[0] * self.BLOCK_WIDTH, pos[1] * self.BLOCK_WIDTH, self.BLOCK_WIDTH, self.BLOCK_WIDTH))

            pygame.display.update()

Window(500, (50, 50), (0, 0, 0), (255, 255, 255))
