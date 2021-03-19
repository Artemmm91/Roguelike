from abc import ABCMeta, abstractmethod
from time import sleep


class AbstractInterface(metaclass=ABCMeta):
    def __new__(cls):
        """ Singleton class, because there is only one interface at one time"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(AbstractInterface, cls).__new__(cls)
        return cls.instance

    @abstractmethod
    def get_event(self):
        pass

    def wait(self, milliseconds):
        sleep(milliseconds)

    @abstractmethod
    def get_event_type(self, event):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def set_screen(self, size, is_full_screen):
        pass

    @abstractmethod
    def get_pressed_keys(self):
        pass

    @abstractmethod
    def get_key(self, event):
        pass

    @abstractmethod
    class Sprite:
        pass

    class GroupSprite:
        def __init__(self):
            self.list = []

        def add(self, sprite):
            self.list.append(sprite)

        def draw(self, display):
            for sprite in self.list:
                sprite.draw(display)

        def update(self, display):
            for sprite in self.list:
                sprite.update(display)

    @abstractmethod
    class Image:
        pass
