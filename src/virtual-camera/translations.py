import numpy as np
from camera import Camera

class Translations:
    @staticmethod
    def get_projection_matrix(fov: float, aspect_ratio: float, near: float, far: float) -> np.array:
        fov_radians = np.deg2rad(fov)
        cot_half_fov = 1 / np.tan(fov_radians / 2)

        projection_matrix = np.array([
            [cot_half_fov, 0, 0, 0],
            [0, cot_half_fov * (1 / aspect_ratio), 0, 0],
            [0, 0, (-far - near) / (far - near), (-2 * far * near) / (far - near)],
            [0, 0, -1, 0]
        ])

        return projection_matrix

    @staticmethod
    def get_view_matrix(camera):
        forward = camera.forward / np.linalg.norm(camera.forward)
        up = camera.up / np.linalg.norm(camera.up)

        right = np.cross(forward, up) / np.linalg.norm(np.cross(forward, up))
        up = np.cross(right, forward)

        translation_matrix = np.eye(4)
        translation_matrix[0:3, 3] = -1 * camera.position

        rotation_matrix = np.eye(4)
        rotation_matrix[0:3, 0] = right
        rotation_matrix[0:3, 1] = up
        rotation_matrix[0:3, 2] = -forward

        view_matrix = np.dot(rotation_matrix, translation_matrix)

        return view_matrix
