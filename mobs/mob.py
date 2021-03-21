from graphics.interface import interface
from setting_files.utils import shift_coord
from setting_files import settings


class Mob(interface.Sprite):
    def __init__(self, frames):
        super().__init__()
        self.coord = None
        self.image_coord = None
        self.image = interface.Image()
        self.frames = frames
        self.current_frame = 0
        self.animation = None
        self.last_image_shift = (0, 0)

    def set_coord(self, coord):
        self.coord = [coord[0], coord[1]]

    def set_image(self, animation_type="still"):
        if self.current_frame >= len(self.frames[animation_type]):
            self.current_frame = 0
        self.image.set_image(self.frames[animation_type][self.current_frame])
        self.current_frame += 1

    def move_image(self, image_coord):
        self.image_coord = image_coord

    def set_animation(self, animation):
        self.animation = animation
        self.current_frame = 0

    def draw(self, display):
        self.image.set_rect(shift_coord(self.image_coord, display.camera, -1))
        interface.blit(display.screen, self.image)

    def walk_animation(self, direction):
        for frame in range(settings.animation_frames):
            for step in range(settings.animation_wait):
                yield
            if direction is not None:
                coefficient = settings.cell_size // settings.animation_frames
                self.last_image_shift = (coefficient * direction[0], coefficient * direction[1])
                self.move_image(shift_coord(self.image_coord, self.last_image_shift))
            self.set_image("walk")
