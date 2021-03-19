from graphics.interface import interface
from setting_files import settings


class Mob(interface.Sprite):
    def __init__(self, frames):
        super().__init__()
        self.coord = None
        self.image = interface.Image()
        self.frames = frames
        self.current_frame = 0

    def set_coord(self, coord):
        self.coord = [coord[0] * settings.cell_size, coord[1] * settings.cell_size]

    def shift_coord(self, shift):
        self.coord[0] += shift[0]
        self.coord[1] += shift[1]

    def set_image(self):
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image.set_image(self.frames[self.current_frame])
        self.current_frame += 1
