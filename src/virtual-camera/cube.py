import numpy as np
from pyrr import Vector3
from constants import *

class Cube:
    def __init__(self, starting_position: Vector3) -> None:
        self.__starting_position = starting_position
        self.__vertices = self.__calculate_initial_vertices_position()

    def __calculate_initial_vertices_position(self) -> list:
        vertices = []
        for normalized_vertices in CubeConstants.VERTICES:
            vertices.append(self.__starting_position + np.array(normalized_vertices) * CubeConstants.CUBE_SIZE)

        return vertices

    def get_projected_cube_points(self, view_matrix, projection_matrix) -> list[tuple]:
        projected_vertices = []

        for vertex in self.__vertices:
            transformed_point = np.dot(view_matrix, np.append(vertex, 1))
            transformed_point = np.dot(projection_matrix, transformed_point)
            transformed_point /= transformed_point[3]

            projected_x = int((transformed_point[0] + 1) * 0.5 * ScreenConstants.SCREEN_WIDTH)
            projected_y = int((1 - transformed_point[1]) * 0.5 * ScreenConstants.SCREEN_HEIGHT)
            projected_vertices.append((projected_x, projected_y))

        return projected_vertices

