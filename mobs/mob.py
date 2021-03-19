from graphics.interface import interface


class Mob(interface.Sprite):
    def __init__(self, frames):
        super().__init__()
        self.coord = None
        self.image = interface.Image()
        self.frames = frames
        self.current_frame = 0
        self.animation = None

    def set_coord(self, coord):
        self.coord = [coord[0], coord[1]]

    def shift_coord(self, shift):
        self.coord[0] += shift[0]
        self.coord[1] += shift[1]

    def set_image(self):
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image.set_image(self.frames[self.current_frame])
        self.current_frame += 1

    def draw(self, display):
        self.image.set_rect((self.coord[0] - display.camera[0], self.coord[1] - display.camera[1]))
        interface.blit(display.screen, self.image)
