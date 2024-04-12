import pygame


class ScreenConstants:
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600
    SCREEN_TITLE: str = "Virtual Camera"
    SCREEN_COLOR: tuple = (0, 0, 0)
    MOVE_STEP: int = 5
    LOOK_STEP: int = 5
    ZOOM_STEP: int = 5
    DEFAULT_FOV: float = 60.0
    DEFAULT_NEAR: float = 5.0
    DEFAULT_FAR: float = 300.0
    AR: float = SCREEN_WIDTH / SCREEN_HEIGHT
    COLORS = {'WHITE': (255, 255, 255), 'BLACK': (0, 0, 0)}
    POLYGON_COLORS = {'BLUE' : (65, 105, 225), 'YELLOW': (255, 255, 102), 'GREEN': (46, 139, 87), 'PURPLE': (153, 102, 204)}
    MINIMUM_FOV = 30
    MAXIMUM_FOV = 90


class ScreenInitializer:
    @staticmethod
    def initialize_app():
        pygame.init()
        pygame.display.set_caption('Virtual camera')
        return pygame.display.set_mode((ScreenConstants.SCREEN_WIDTH, ScreenConstants.SCREEN_HEIGHT))


class CubeConstants:
    VERTICES = [[-1, -1, -1],
                [1, -1, -1],
                [1, 1, -1],
                [-1, 1, -1],
                [-1, -1, 1],
                [1, -1, 1],
                [1, 1, 1],
                [-1, 1, 1]]

    FACES = [[0, 1, 5, 4],
             [2, 3, 7, 6],
             [0, 3, 7, 4],
             [1, 2, 6, 5],
             [0, 1, 2, 3],
             [4, 5, 6, 7]]

    CUBE_SIZE = 20

    EDGES = [(0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]

    STARTING_POSITIONS = [
        [0.0, 0.0, 100.0],
        [60.0, 0.0, 100.0],
        [60.0, 0.0, 200.0],
        [60.0, 0.0, 200.0],
        [0.0, 0.0, 200.0]
    ]
