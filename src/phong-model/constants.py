import numpy as np
import pygame


class ScreenConstants:
    SCREEN_WIDTH: int = 400
    SCREEN_HEIGHT: int = 400
    SCREEN_TITLE: str = "Phong model"
    SCREEN_COLOR: tuple = (0, 0, 0)
    SPHERE_RADIUS = 100
    SPHERE_CENTER: tuple = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2)
    DEFAULT_MATERIAL: tuple = (0.4, 0.9, 0.9)
    CHALK_MATERIAL: tuple = (0.4, 1, 0.01)
    WOOD_MATERIAL: tuple = (0.4, 0.8, 0.4)
    METAL_MATERIAL: tuple = (0.4, 0.2, 0.9)
    PLASTIC_MATERIAL: tuple = (0.4, 0.4, 0.8)
    STEP_SIZE = 50
    COLOR_SATURATION = 0.4
    INITIAL_POSITION_OF_LIGHT = np.array([250, 200, 0], dtype=float)
    INITIAL_POSITION_OF_OBSERVER = np.array([200, 200, 0], dtype=float)
    MATERIALS = [('DEFAULT', DEFAULT_MATERIAL), ('CHALK', CHALK_MATERIAL), ('WOOD', WOOD_MATERIAL),
                 ('METAL', METAL_MATERIAL), ('PLASTIC', PLASTIC_MATERIAL)]
    Ia = 1
    Ip = 0.6
    n = 30

    SPHERE_COLORS = {
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
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
        'BEIGE': (245, 245, 220),
        'GRAY': (200, 200, 200)
    }


class ScreenInitializer:
    @staticmethod
    def initialize_app():
        pygame.init()
        pygame.display.set_caption('Phong model')
        return pygame.display.set_mode((ScreenConstants.SCREEN_WIDTH, ScreenConstants.SCREEN_HEIGHT))
