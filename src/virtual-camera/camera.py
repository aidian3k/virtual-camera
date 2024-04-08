import numpy as np
from pyrr import Vector3, Quaternion


class Camera:
    def __init__(self):
        self.position = Vector3([0.0, 0.0, 0.0], dtype=float)
        self.up = Vector3([0.0, 1.0, 0.0], dtype=float)
        self.forward = Vector3([0.0, 0.0, 1.0], dtype=float)

    def get_right_vector(self) -> np.array:
        return np.cross(self.forward, self.up)

    def look_left(self, angle):
        rotation_quaternion = Quaternion.from_axis_rotation(self.up, np.radians(angle))
        self.forward = rotation_quaternion * self.forward
        self.forward = Vector3(self.forward.normalized, dtype=float)

    def look_right(self, angle):
        rotation_quaternion = Quaternion.from_axis_rotation(self.up, np.radians(-angle))
        self.forward = rotation_quaternion * self.forward
        self.forward = Vector3(self.forward.normalized, dtype=float)

    def look_up(self, angle):
        right = self.get_right_vector()
        rotation_quaternion = Quaternion.from_axis_rotation(right, np.radians(angle))
        self.forward = rotation_quaternion * self.forward
        self.forward = Vector3(self.forward.normalized, dtype=float)

    def look_down(self, angle):
        right = self.get_right_vector()
        rotation_quaternion = Quaternion.from_axis_rotation(right, np.radians(-angle))
        self.forward = rotation_quaternion * self.forward
        self.forward = Vector3(self.forward.normalized, dtype=float)

    def tilt_left(self, angle):
        rotation_quaternion = Quaternion.from_axis_rotation(self.forward, np.radians(angle))
        self.up = rotation_quaternion * self.up
        self.up = Vector3(self.up.normalized, dtype=float)

    def tilt_right(self, angle):
        rotation_quaternion = Quaternion.from_axis_rotation(self.forward, np.radians(-angle))
        self.up = rotation_quaternion * self.up
        self.up = Vector3(self.up.normalized, dtype=float)

