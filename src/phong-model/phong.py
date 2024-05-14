import math
from colorsys import hls_to_rgb

import numpy as np
import pygame

from constants import ScreenConstants


class PhongModelEngine:
    def __init__(self, screen):
        self.__screen = screen
        self.__light_position = ScreenConstants.INITIAL_POSITION_OF_LIGHT
        self.__observer_position = ScreenConstants.INITIAL_POSITION_OF_OBSERVER
        self.__current_material_index = 0
        self.__current_material = ScreenConstants.MATERIALS[self.__current_material_index]

    def run(self) -> None:
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT:
                        if self.__current_material_index + 1 >= len(ScreenConstants.MATERIALS):
                            self.__current_material_index = 0
                        else:
                            self.__current_material_index += 1

                        self.__current_material = ScreenConstants.MATERIALS[self.__current_material_index]
                elif event.type == pygame.K_SPACE:
                    self.__light_position = ScreenConstants.INITIAL_POSITION_OF_LIGHT

            self.__handle_key_pressing(pygame.key.get_pressed())
            self.__update_screen()

        pygame.quit()

    def __update_screen(self) -> None:
        self.__screen.fill(ScreenConstants.SPHERE_COLORS['GRAY'])
        self.__draw_illuminated_sphere()
        self.__display_currently_chosen_material()

        pygame.display.flip()

    def __draw_illuminated_sphere(self) -> None:
        for x in range(ScreenConstants.SCREEN_WIDTH):
            for y in range(ScreenConstants.SCREEN_HEIGHT):
                z = self.__calculate_z_sphere(x, y)

                if z:
                    illumination = self.__calculate_light_illumination(x, y, int(z))
                    red, green, blue = hls_to_rgb(0.5, illumination, ScreenConstants.COLOR_SATURATION)
                    color = (255 * red, 255 * green, 255 * blue)
                    self.__screen.set_at((x, ScreenConstants.SCREEN_HEIGHT - y), color)

    def __calculate_light_illumination(self, x: int, y: int, z: int) -> float:
        N = self.__normalize_vector(np.array(ScreenConstants.SPHERE_CENTER) - np.array([x, y, z]))
        L = self.__normalize_vector(np.array([x, y, z]) - self.__light_position)
        V = self.__normalize_vector(np.array([x, y, z]) - self.__observer_position)
        R = self.__normalize_vector(np.subtract(np.multiply(np.multiply(N, 2), np.multiply(N, L)), L))

        r = self.__calculate_light_source_distance_from_point(x, y, z) / ScreenConstants.SPHERE_RADIUS
        K_c = 0.1
        K_l = 0.2
        K_q = 0.25

        f_att = min(1 / (K_c + K_l * r + K_q * r ** 2), 1.0)

        illumination = (f_att * ScreenConstants.Ip *
                        self.__current_material[1][1] * max(np.dot(N, L), 0) + f_att * ScreenConstants.Ip *
                        self.__current_material[1][2] * max(np.dot(R, V), 0) ** ScreenConstants.n)

        return min(illumination, 1)

    def __calculate_light_source_distance_from_point(self, x, y, z) -> float:
        x_difference = self.__light_position[0] - x
        y_difference = self.__light_position[1] - y
        z_difference = self.__light_position[2] - z

        return math.sqrt(x_difference ** 2 + y_difference ** 2 + z_difference ** 2)

    def __normalize_vector(self, vector: np.array) -> np.array:
        length = np.linalg.norm(vector)
        if length == 0:
            return vector

        return vector / length

    def __check_if_light_inside_sphere(self, x, y, z) -> bool:
        r = math.sqrt((x - ScreenConstants.SPHERE_CENTER[0]) ** 2 + (y - ScreenConstants.SPHERE_CENTER[1]) ** 2 + (
                z - ScreenConstants.SPHERE_CENTER[2]) ** 2)

        return r > ScreenConstants.SPHERE_RADIUS

    def __calculate_z_sphere(self, x: int, y: int) -> float:
        b = -2 * ScreenConstants.SPHERE_CENTER[2]
        c = ScreenConstants.SPHERE_CENTER[2] ** 2 + (x - ScreenConstants.SPHERE_CENTER[0]) ** 2 + (
                y - ScreenConstants.SPHERE_CENTER[1]) ** 2 - ScreenConstants.SPHERE_RADIUS ** 2
        delta = b ** 2 - 4 * c

        if delta == 0:
            return -b / 2
        elif delta > 0:
            return min((math.sqrt(delta) - b) / 2, (-math.sqrt(delta) - b) / 2)

    def __display_currently_chosen_material(self):
        size_of_font, vertical_position_of_the_text = 36, 40
        font = pygame.font.SysFont(None, size_of_font)
        text = font.render(f"Material: {self.__current_material[0]}", True, ScreenConstants.SPHERE_COLORS['WHITE'])
        text_rect = text.get_rect(center=(ScreenConstants.SCREEN_WIDTH // 2, vertical_position_of_the_text))
        self.__screen.blit(text, text_rect)

    def __handle_key_pressing(self, pressed_keys) -> None:
        if pressed_keys[pygame.K_UP] and self.__check_if_light_inside_sphere(self.__light_position[0],
                                                                             self.__light_position[1],
                                                                             self.__light_position[
                                                                                 2] + ScreenConstants.STEP_SIZE):
            self.__light_position[2] += ScreenConstants.STEP_SIZE
        elif pressed_keys[pygame.K_DOWN] and self.__check_if_light_inside_sphere(self.__light_position[0],
                                                                                 self.__light_position[1],
                                                                                 self.__light_position[
                                                                                     2] - ScreenConstants.STEP_SIZE):
            self.__light_position[2] -= ScreenConstants.STEP_SIZE
        elif pressed_keys[pygame.K_a] and self.__check_if_light_inside_sphere(
                self.__light_position[0] - ScreenConstants.STEP_SIZE, self.__light_position[1],
                self.__light_position[2]):
            self.__light_position[0] -= ScreenConstants.STEP_SIZE
        elif pressed_keys[pygame.K_d] and self.__check_if_light_inside_sphere(
                self.__light_position[0] + ScreenConstants.STEP_SIZE, self.__light_position[1],
                self.__light_position[2]):
            self.__light_position[0] += ScreenConstants.STEP_SIZE
        elif pressed_keys[pygame.K_w] and self.__check_if_light_inside_sphere(self.__light_position[0],
                                                                              self.__light_position[
                                                                                  1] + ScreenConstants.STEP_SIZE,
                                                                              self.__light_position[2]):
            self.__light_position[1] += ScreenConstants.STEP_SIZE
        elif pressed_keys[pygame.K_s] and self.__check_if_light_inside_sphere(self.__light_position[0],
                                                                              self.__light_position[
                                                                                  1] - ScreenConstants.STEP_SIZE,
                                                                              self.__light_position[2]):
            self.__light_position[1] -= ScreenConstants.STEP_SIZE
