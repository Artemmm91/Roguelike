from setting_files import settings


class Display:
    def __init__(self, interface):
        self.interface = interface
        self.screen = self.interface.set_display(settings.SCREEN_SIZE, settings.FULLSCREEN_DEFAULT)
        self.camera = [0, 0]

    def fullscreen(self):
        pass

    def update(self):
        self.interface.update()

    def screen_fill(self, color):
        self.screen.fill(color)

    def draw(self, sprite):
        self.interface.blit(self.screen, sprite.image)

    def draw_image(self, image):
        self.interface.blit(self.screen, image)

    def shift_camera(self, shift):
        self.camera[0] += shift[0]
        self.camera[1] += shift[1]
