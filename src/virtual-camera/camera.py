import numpy as np
from pyrr import Vector3, Quaternion


class Camera:
    def __init__(self):
        self.position = Vector3([30.0, 0.0, 250], dtype=float)
        self.yaw = 0
        self.pitch = 0
        self.roll = 0

    def get_direction_vector(self):
        direction = np.array([
            np.cos(self.pitch) * np.sin(-self.yaw),
            np.sin(self.pitch),
            np.cos(self.pitch) * np.cos(-self.yaw)
        ])
        return direction


