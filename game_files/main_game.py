from game_files.abstract_process import Process
from setting_files import settings
from map.map_generator import generate_map
from display.display import Display


class MainGame(Process):
    def __init__(self):
        super().__init__()
        self.window_close = False
        self.display = Display(self.interface)
        self.map = None
        self.hero_acted = False
        self.sprites = self.interface.GroupSprite()

    def new_level(self):
        self.map = generate_map()
        self.map.spawn_monsters()
        self.map.spawn_hero()
        self.map.render_map()

        for monster in self.map.mobs.values():
            self.sprites.add(monster)

        self.map.hero.center_camera(self.display)

    def main_loop(self):
        """ Main loop of program - processing each tick/frame of game """
        self.new_level()
        while not self.window_close:
            self.process_events()
            self.game_logic()
            self.draw()
            self.interface.wait(settings.frame_wait)

    def is_animation(self):
        if self.map.hero.animation:
            return True
        for m in self.map.mobs.values():
            if m.animation:
                return True
        return False

    def process_events(self):
        """ Processing all events - clicking buttons - and respectively moving objects by commands """
        events = self.interface.Event.get_event()
        for event in events:
            event_type = self.interface.Event.get_event_type(event)
            if event_type == settings.quit_flag:
                self.window_close = True
            if event_type == settings.keydown_flag:
                event_key = self.interface.Event.get_key(event)
                if event_key == settings.escape_key:
                    self.display.fullscreen()
                if not self.is_animation():
                    self.hero_acted = self.map.hero.act(event_key, self.map)

    def game_logic(self):
        """ Automatic move of objects/units/monsters, checking collisions, and other game logic """
        if not self.is_animation() and self.hero_acted:
            current_monsters = list(self.map.mobs.values())
            for monster in current_monsters:
                if monster != self.map.hero:
                    monster.act(self.map)
            # monsters turn
            self.hero_acted = False

    def draw(self):
        """ Drawing all objects to the window """
        self.display.screen_fill(settings.colors["BLACK"])

        self.sprites.update(self.display)
        self.map.update(self.display)

        self.map.draw(self.display)
        self.sprites.draw(self.display)
        self.display.update()
