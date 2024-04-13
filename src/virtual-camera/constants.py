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
    POLYGON_COLORS = colors = {
        'BLUE': (0, 0, 255),
        'YELLOW': (255, 255, 0),
        'GREEN': (0, 255, 0),
        'PURPLE': (128, 0, 128),
        'ORANGE': (255, 165, 0),
        'RED': (255, 0, 0),
        'PINK': (255, 192, 203),
        'BROWN': (165, 42, 42),
        'CYAN': (0, 255, 255),
        'MAGENTA': (255, 0, 255),
        'GOLD': (255, 215, 0),
        'SILVER': (192, 192, 192),
        'MAROON': (128, 0, 0),
        'NAVY': (0, 0, 128),
        'TEAL': (0, 128, 128),
        'OLIVE': (128, 128, 0),
        'LIME': (0, 255, 0),
        'AQUA': (0, 255, 255),
        'FUCHSIA': (255, 0, 255),
        'KHAKI': (240, 230, 140),
        'TURQUOISE': (64, 224, 208),
        'INDIGO': (75, 0, 130),
        'VIOLET': (238, 130, 238),
        'CRIMSON': (220, 20, 60),
        'BEIGE': (245, 245, 220)
    }
    MINIMUM_FOV = 30
    MAXIMUM_FOV = 90
    CIRCLE_SIZE = 5


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

    FACES = [[0, 1, 2], [0, 2, 3],  # Front face
             [4, 5, 6], [4, 6, 7],  # Back face
             [1, 5, 6], [1, 6, 2],  # Right face
             [0, 4, 7], [0, 7, 3],  # Left face
             [3, 2, 6], [3, 6, 7],  # Top face
             [0, 1, 5], [0, 5, 4]]  # Bottom face

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
