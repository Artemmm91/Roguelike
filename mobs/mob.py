from graphics.interface import InterfacePyGame
from setting_files.utils import shift_coord, make_splitting
from setting_files import settings


class Mob:
    def __init__(self, frames):
        super().__init__()
        self.coord = None
        self.image_coord = None
        self.image = InterfacePyGame.Image()
        self.frames = frames
        self.current_frame = 0
        self.animation = None
        self.target_coord = None

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
        # self.current_frame = 0  # while there is no walk animation

    def draw(self, display):
        self.image.set_rect(shift_coord(self.image_coord, display.camera, -1))
        InterfacePyGame().blit(display.screen, self.image)

    def walk_animation(self, direction):
        shift_list = make_splitting(settings.cell_size, settings.animation_frames, direction)
        for shift in shift_list:
            yield
            self.move_image(shift_coord(self.image_coord, shift))
            self.set_image("walk")

    def update(self, display):
        if self.animation:
            try:
                next(self.animation)
            except StopIteration:
                self.set_animation(None)
        else:
            self.set_image()
