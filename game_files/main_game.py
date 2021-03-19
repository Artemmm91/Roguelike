from game_files.abstract_process import Process
from setting_files import settings
from map.map_generator import generate_map
from mobs.hero import Hero
from display.display import Display


class MainGame(Process):
    def __init__(self):
        super().__init__()
        self.window_close = False
        self.display = Display(self.interface)
        self.map = None
        self.hero = Hero()
        self.hero_acted = False

    def new_level(self):
        self.map = generate_map()
        self.map.render_map()
        self.hero.set_coord(self.map.hero_coord)

    def main_loop(self):
        """ Main loop of program - processing each tick/frame of game """
        self.new_level()
        while not self.window_close:
            self.process_events()
            self.game_logic()
            self.draw()
            self.interface.wait(settings.frame_wait)

    def process_events(self):
        """ Processing all events - clicking buttons - and respectively moving objects by commands """
        events = self.interface.get_event()
        for event in events:
            event_type = self.interface.get_event_type(event)
            if event_type == settings.quit_flag:
                self.window_close = True
            if event_type == settings.keydown_flag:
                event_key = self.interface.get_key(event)
                if event_key == settings.escape_key:
                    self.display.fullscreen()
                if not self.hero.animation:
                    self.hero_acted = self.hero.act(event_key, self.map)

    def game_logic(self):
        """ Automatic move of objects/units/monsters, checking collisions, and other game logic """
        if not self.hero.animation and self.hero_acted:
            # monsters turn
            self.hero_acted = False

    def draw(self):
        """ Drawing all objects to the window """
        self.display.screen_fill(settings.BLACK)

        self.hero.update(self.display)
        self.map.update(self.display)

        self.map.draw(self.display)
        self.display.draw(self.hero)
        self.display.update()
