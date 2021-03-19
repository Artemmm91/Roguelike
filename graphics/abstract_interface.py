from abc import ABCMeta, abstractmethod
from time import sleep


class AbstractInterface(metaclass=ABCMeta):
    def __new__(cls):
        """ Singleton class, because there is only one interface at one time"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(AbstractInterface, cls).__new__(cls)
        return cls.instance

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def set_display(self, size, is_full_screen):
        pass

    @abstractmethod
    def load_image(self, filename):
        pass

    @staticmethod
    @abstractmethod
    def blit(screen, image):
        pass

    def wait(self, milliseconds):
        sleep(milliseconds)

    @abstractmethod
    class Event:
        @staticmethod
        @abstractmethod
        def get_event():
            pass

        @staticmethod
        @abstractmethod
        def get_event_type(event):
            pass

        @staticmethod
        @abstractmethod
        def get_pressed_keys():
            pass

        @staticmethod
        @abstractmethod
        def get_key(event):
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
        @abstractmethod
        def set_image(self, img):
            pass

        @abstractmethod
        def move_rect(self, shift):
            pass

        @abstractmethod
        def set_rect(self, left):
            pass

        @abstractmethod
        def subsurface(self, rect):
            pass

        @abstractmethod
        def get_size(self):
            pass

        @abstractmethod
        def scale(self, new_size):
            pass

        @abstractmethod
        def merge(self, image):
            pass
