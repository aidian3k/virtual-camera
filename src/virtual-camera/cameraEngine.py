import pyrr
from constants import *
from cube import Cube
from camera import Camera
from translations import Translations


class VirtualCameraEngine:
    def __init__(self, camera: Camera, screen):
        self.camera = camera
        self.__fov = ScreenConstants.DEFAULT_FOV
        self.__screen = screen
        self.view = Translations.get_view_matrix(camera)
        self.projection = Translations.get_projection_matrix(ScreenConstants.DEFAULT_FOV, ScreenConstants.AR,
                                                             ScreenConstants.DEFAULT_NEAR, ScreenConstants.DEFAULT_FAR)
        self.__scene_cubes = []

    def run(self) -> None:
        running = True
        self.__scene_cubes: list[Cube] = self.__initialize_initial_cubes()

        self.__initialize_initial_cubes()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.__screen.fill(ScreenConstants.COLORS['BLACK'])
                    currently_pressed_key = event.key
                    self.__handle_key_pressing(currently_pressed_key)

                self.__update_screen()

        pygame.quit()

    def __update_screen(self) -> None:
        self.view = Translations.get_view_matrix(self.camera)
        self.projection = Translations.get_projection_matrix(self.__fov, ScreenConstants.AR,
                                                             ScreenConstants.DEFAULT_NEAR, ScreenConstants.DEFAULT_FAR)
        self.__draw_cubes_on_screen()

        pygame.display.flip()

    def __handle_key_pressing(self, event_key: int) -> None:
        self.__handle_backward_forward_left_right(event_key)
        self.__handle_zooming(event_key)
        self.__handle_looking(event_key)
        self.__handle_reset(event_key)

    def __handle_backward_forward_left_right(self, event_key: int) -> None:
        if event_key == pygame.K_w:
            self.camera.position += pyrr.vector3.normalize(self.camera.forward) * 10
        elif event_key == pygame.K_s:
            self.camera.position -= pyrr.vector3.normalize(self.camera.forward) * 10
        elif event_key == pygame.K_a:
            self.camera.position -= pyrr.vector3.normalize(self.camera.forward.cross(self.camera.up)) * 10
        elif event_key == pygame.K_d:
            self.camera.position += pyrr.vector3.normalize(self.camera.forward.cross(self.camera.up)) * 10
        elif event_key == pygame.K_UP:
            self.camera.position += pyrr.vector3.normalize(self.camera.up) * 10
        elif event_key == pygame.K_DOWN:
            self.camera.position -= pyrr.vector3.normalize(self.camera.up) * 10

    def __handle_zooming(self, event_key: int) -> None:
        if event_key == pygame.K_EQUALS:
            if self.__fov > ScreenConstants.MINIMUM_FOV:
                self.__fov -= 5
        elif event_key == pygame.K_MINUS:
            if self.__fov < ScreenConstants.MAXIMUM_FOV:
                self.__fov += 5

    def __handle_looking(self, event_key: int) -> None:
        if event_key == pygame.K_i:
            self.camera.look_up(5)
        elif event_key == pygame.K_j:
            self.camera.look_right(5)
        elif event_key == pygame.K_k:
            self.camera.look_down(5)
        elif event_key == pygame.K_l:
            self.camera.look_left(5)
        elif event_key == pygame.K_u:
            self.camera.tilt_left(5)
        elif event_key == pygame.K_o:
            self.camera.tilt_right(5)

    def __handle_reset(self, event_key: int) -> None:
        if event_key == pygame.K_SPACE:
            self.camera = Camera()

    def __draw_cubes_on_screen(self) -> None:
        for cube in self.__scene_cubes:
            projected_points = cube.get_projected_cube_points(self.view, self.projection)

            for edge in CubeConstants.EDGES:
                if projected_points[edge[0]] is not None and projected_points[edge[1]] is not None:
                    pygame.draw.line(self.__screen, ScreenConstants.COLORS['WHITE'], projected_points[edge[0]],
                                 projected_points[edge[1]])

    def __initialize_initial_cubes(self) -> list[Cube]:
        cubes = []
        for starting_cube_position in CubeConstants.STARTING_POSITIONS:
            cubes.append(Cube(starting_cube_position))

        return cubes