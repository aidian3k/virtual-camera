import pygame.event
import pyrr
from pyrr import Vector3

from constants import *
from cube import Cube
from camera import Camera
from polygon import Polygon
from translations import Translations


class VirtualCameraEngine:
    def __init__(self, camera: Camera, screen):
        self.camera = camera
        self.__fov = ScreenConstants.DEFAULT_FOV
        self.__screen = screen
        self.projection = Translations.get_projection_matrix(ScreenConstants.DEFAULT_FOV, ScreenConstants.AR,
                                                             ScreenConstants.DEFAULT_NEAR, ScreenConstants.DEFAULT_FAR)
        self.__scene_cubes = []
        self.__is_drawing_polygons = False

    def run(self) -> None:
        running = True
        self.__scene_cubes: list[Cube] = self.__initialize_initial_cubes()
        self.__initialize_initial_cubes()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT:
                        self.__is_drawing_polygons = not self.__is_drawing_polygons

                self.__screen.fill(ScreenConstants.COLORS['BLACK'])
                self.__handle_key_pressing(pygame.key.get_pressed())

                self.__update_screen()

        pygame.quit()

    def __update_screen(self) -> None:
        self.projection = Translations.get_projection_matrix(self.__fov, ScreenConstants.AR,
                                                             ScreenConstants.DEFAULT_NEAR, ScreenConstants.DEFAULT_FAR)
        self.__draw_cubes_on_screen()

        pygame.display.flip()

    def __handle_key_pressing(self, pressed_keys) -> None:
        self.__handle_backward_forward_left_right(pressed_keys)
        self.__handle_zooming(pressed_keys)
        self.__handle_looking(pressed_keys)
        self.__handle_reset(pressed_keys)

    def __handle_backward_forward_left_right(self, pressed_keys: list[bool]) -> None:
        if pressed_keys[pygame.K_w]:
            self.camera.position -= self.camera.get_direction_vector() * ScreenConstants.MOVE_STEP
        elif pressed_keys[pygame.K_s]:
            self.camera.position += self.camera.get_direction_vector() * ScreenConstants.MOVE_STEP
        elif pressed_keys[pygame.K_a]:
            self.camera.position[0] -= ScreenConstants.MOVE_STEP
        elif pressed_keys[pygame.K_d]:
            self.camera.position[0] += ScreenConstants.MOVE_STEP
        elif pressed_keys[pygame.K_UP]:
            self.camera.position[1] += ScreenConstants.MOVE_STEP
        elif pressed_keys[pygame.K_DOWN]:
            self.camera.position[1] -= ScreenConstants.MOVE_STEP

    def __handle_zooming(self, pressed_keys: list[bool]) -> None:
        if pressed_keys[pygame.K_EQUALS]:
            if self.__fov > ScreenConstants.MINIMUM_FOV:
                self.__fov -= ScreenConstants.ZOOM_STEP
        elif pressed_keys[pygame.K_MINUS]:
            if self.__fov < ScreenConstants.MAXIMUM_FOV:
                self.__fov += ScreenConstants.ZOOM_STEP

    def __handle_looking(self, pressed_keys: list[bool]) -> None:
        if pressed_keys[pygame.K_i]:
            self.camera.pitch -= 0.1
        elif pressed_keys[pygame.K_j]:
            self.camera.yaw -= 0.1
        elif pressed_keys[pygame.K_k]:
            self.camera.pitch += 0.1
        elif pressed_keys[pygame.K_l]:
            self.camera.yaw += 0.1
        elif pressed_keys[pygame.K_u]:
            self.camera.roll -= 0.1
        elif pressed_keys[pygame.K_o]:
            self.camera.roll += 0.1

    def __handle_reset(self, pressed_keys: list[bool]) -> None:
        if pressed_keys[pygame.K_SPACE]:
            self.camera = Camera()

    def __draw_cubes_on_screen(self) -> None:
        for cube in self.__scene_cubes:
            if not self.__is_drawing_polygons:
                projected_points = cube.get_projected_cube_points(self.camera, self.projection)

                for edge in CubeConstants.EDGES:
                    starting_vertex = projected_points[edge[0]]
                    ending_vertex = projected_points[edge[1]]

                    if starting_vertex is not None and ending_vertex is not None:
                        pygame.draw.circle(self.__screen, ScreenConstants.POLYGON_COLORS['PURPLE'], starting_vertex, ScreenConstants.CIRCLE_SIZE)
                        pygame.draw.circle(self.__screen, ScreenConstants.POLYGON_COLORS['PURPLE'], ending_vertex, ScreenConstants.CIRCLE_SIZE)

                        pygame.draw.line(self.__screen, ScreenConstants.COLORS['WHITE'], projected_points[edge[0]],
                                         projected_points[edge[1]])
            else:
                all_cubes_polygons: list[Polygon] = [polygon for cube in self.__scene_cubes for polygon in cube.polygons]
                sorted_polygons_by_distance_of_observer = self.sort_polygons_by_distance_of_observer(all_cubes_polygons, self.camera.position)

                for polygon in sorted_polygons_by_distance_of_observer:
                    projected_polygon_points = polygon.get_projected_polygon_points(self.camera, self.projection)

                    if all(projected_polygon_points):
                        pygame.draw.polygon(self.__screen, polygon.color, projected_polygon_points)

    def sort_polygons_by_distance_of_observer(self, polygons: list[Polygon], observer: Vector3) -> list[Polygon]:
        distances = []

        for polygon in polygons:
            distances.append((polygon, polygon.get_distance_from_observer(observer)))

        sorted_polygons = [polygon for polygon, _ in sorted(distances, key=lambda x: x[1])]

        return sorted_polygons

    def __initialize_initial_cubes(self) -> list[Cube]:
        cubes = []
        for starting_cube_position in CubeConstants.STARTING_POSITIONS:
            cubes.append(Cube(starting_cube_position))

        return cubes
