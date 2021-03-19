from setting_files import settings


class Display:
    def __init__(self, interface):
        self.interface = interface
        self.screen = self.interface.set_screen(settings.SCREEN_SIZE, settings.FULLSCREEN_DEFAULT)
        self.camera = [0, 0]

    def fullscreen(self):
        pass

    def update(self):
        self.interface.update()

    def screen_fill(self, color):
        self.screen.fill(color)

    def draw(self, sprite):
        self.screen.blit(sprite.image.image, sprite.image.rect)

    def draw_image(self, image):
        self.screen.blit(image.image, image.rect)

    def shift_camera(self, shift):
        self.camera[0] += shift[0]
        self.camera[1] += shift[1]
