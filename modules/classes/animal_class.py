import abc 


class Animal(abc.ABC):

    def __init__(self, name: str, color: str, height: int=50, breed: str=None):
        self._name = name
        self._color = color
        self._height = height
        self._breed = breed
        self._sound = 'I dont know who i am'
        self._speed = lambda: 13 if self._height <= 20 else 17

    def __repr__(self):
        return f'{type(self)}'

    @abc.abstractmethod
    def get_name(self):
        pass

    def get_color(self):
        pass

    def get_height(self):
        pass

    def voice(self):
        pass
             
    def move(self):
        pass

    def __add__(self, other):
        pass

    def set_name(self):
        pass

    def get_bigger(self):
        pass
