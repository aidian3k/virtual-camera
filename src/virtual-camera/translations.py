import numpy as np


class Translations:
    @staticmethod
    def get_projection_matrix(fov: float, aspect_ratio: float, near: float, far: float) -> np.array:
        fov_radians = np.deg2rad(fov)
        cot_half_fov = 1 / np.tan(fov_radians / 2)

        projection_matrix = np.array([
            [cot_half_fov, 0, 0, 0],
            [0, cot_half_fov * (1 / aspect_ratio), 0, 0],
            [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
            [0, 0, -1, 0]
        ])

        return projection_matrix

    @staticmethod
    def get_x_camera_rotation(angle: float) -> np.array:
        cos_rotation = np.cos(angle)
        sin_rotation = np.sin(angle)

        return np.array([[1, 0, 0],
                         [0, cos_rotation, -sin_rotation],
                         [0, sin_rotation, cos_rotation]])

    @staticmethod
    def get_y_camera_rotation(angle: float) -> np.array:
        cos_rotation = np.cos(angle)
        sin_rotation = np.sin(angle)

        return np.array([[cos_rotation, 0, sin_rotation],
                         [0, 1, 0],
                         [-sin_rotation, 0, cos_rotation]])

    @staticmethod
    def get_z_camera_rotation(angle: float) -> np.array:
        cos_rotation = np.cos(angle)
        sin_rotation = np.sin(angle)

        return np.array([[cos_rotation, -sin_rotation, 0],
                         [sin_rotation, cos_rotation, 0],
                         [0, 0, 1]])
