from constants import ScreenInitializer
from phong import PhongModelEngine

if __name__ == '__main__':
    screen = ScreenInitializer.initialize_app()
    phong_model_engine = PhongModelEngine(screen)

    phong_model_engine.run()