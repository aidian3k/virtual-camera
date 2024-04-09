from camera import Camera
from constants import ScreenInitializer
from cameraEngine import VirtualCameraEngine

if __name__ == "__main__":
    camera = Camera()
    screen = ScreenInitializer.initialize_app()
    camera_engine = VirtualCameraEngine(camera, screen)
    camera_engine.run()


