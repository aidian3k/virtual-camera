import numpy as np
import pygame

from polygon import Polygon
from camera import Camera


def normalize_vector(vector: np.array):
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector

    return vector / norm


def normalize_polygon(polygon: Polygon):
    edgeOne = polygon.vertices[1][:3] - polygon.vertices[0][:3]
    edgeTwo = polygon.vertices[2][:3] - polygon.vertices[0][:3]

    return normalize_vector(np.cross(edgeOne, edgeTwo))


def implicit_plane_function(point, polygon):
    n = normalize_polygon(polygon)

    return n @ (point - polygon.vertices[0][:3])


def draw_polygon(screen, camera, projection, polygon):
    projected_polygon_points = polygon.get_projected_polygon_points(camera, projection)

    if all(projected_polygon_points):
        pygame.draw.polygon(screen, polygon.color, projected_polygon_points)


class BspTree:
    def __init__(self, starting_polygon: Polygon):
        self.polygon = starting_polygon
        self.left: BspTree = None
        self.right: BspTree = None

    def draw_polygons_recursively(self, camera: Camera, projection_matrix: np.array, screen) -> None:
        p = implicit_plane_function(camera.position, self.polygon)

        if p < 0:
            if self.left is not None:
                self.left.draw_polygons_recursively(camera, projection_matrix, screen)

            draw_polygon(screen, camera, projection_matrix, self.polygon)

            if self.right is not None:
                self.right.draw_polygons_recursively(camera, projection_matrix, screen)
        else:
            if self.right is not None:
                self.right.draw_polygons_recursively(camera, projection_matrix, screen)

            draw_polygon(screen, camera, projection_matrix, self.polygon)

            if self.left is not None:
                self.left.draw_polygons_recursively(camera, projection_matrix, screen)

    def add(self, polygon: Polygon):
        triangle_vertices = polygon.vertices

        first_node = triangle_vertices[0]
        second_node = triangle_vertices[1]
        third_node = triangle_vertices[2]

        f_a = implicit_plane_function(first_node[:3], self.polygon)
        f_b = implicit_plane_function(second_node[:3], self.polygon)
        f_c = implicit_plane_function(third_node[:3], self.polygon)

        if abs(f_a) < np.finfo(float).eps:
            f_a = 0
        if abs(f_b) < np.finfo(float).eps:
            f_b = 0
        if abs(f_c) < np.finfo(float).eps:
            f_c = 0
        if f_a <= 0 and f_b <= 0 and f_c <= 0:
            if self.right is None:
                self.right = BspTree(polygon)
            else:
                self.right.add(polygon)
        elif f_a >= 0 and f_b >= 0 and f_c >= 0:
            if self.left is None:
                self.left = BspTree(polygon)
            else:
                self.left.add(polygon)
