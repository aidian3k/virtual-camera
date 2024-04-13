import numpy as np
from pyrr import Vector3
from constants import ScreenConstants
from translations import Translations


class Polygon:
    def __init__(self, vertices: list[Vector3], color: tuple):
        self.vertices = vertices
        self.color = color

    def __get_center_of_gravity(self) -> np.array:
        num_vertices = len(self.vertices)
        if num_vertices == 0:
            return None

        sum_x = sum_y = sum_z = 0

        for vertex in self.vertices:
            sum_x += vertex[0]
            sum_y += vertex[1]
            sum_z += vertex[2]

        center_x = sum_x / num_vertices
        center_y = sum_y / num_vertices
        center_z = sum_z / num_vertices

        return np.array([center_x, center_y, center_z])

    def get_distance_from_observer(self, position: Vector3) -> float:
        center_of_gravity = self.__get_center_of_gravity()

        return (position[0] - center_of_gravity[0]) ** 2 + (position[1] - center_of_gravity[1]) ** 2 + (
                    position[2] - center_of_gravity[2]) ** 2

    def get_projected_polygon_points(self, camera, projection_matrix) -> list[tuple]:
        projected_vertices = []

        for vertex in self.vertices:
            normalized_vertex_to_camera = vertex - camera.position

            rotated_point = np.dot(Translations.get_y_camera_rotation(camera.yaw), normalized_vertex_to_camera)
            rotated_point = np.dot(Translations.get_x_camera_rotation(camera.pitch), rotated_point)
            rotated_point = np.dot(Translations.get_z_camera_rotation(camera.roll), rotated_point)

            transformed_point = np.dot(projection_matrix, np.append(rotated_point, 1))

            if transformed_point[3] > 0:
                transformed_point /= transformed_point[3]

                projected_x = int((transformed_point[0] + 1) * 0.5 * ScreenConstants.SCREEN_WIDTH)
                projected_y = int((1 - transformed_point[1]) * 0.5 * ScreenConstants.SCREEN_HEIGHT)
                projected_vertices.append((projected_x, projected_y))
            else:
                projected_vertices.append(None)

        return projected_vertices
