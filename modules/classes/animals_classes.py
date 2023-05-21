import modules.classes.animal_class as a
import time
import modules.classes.decorators as d

class Dog(a.Animal):

    def __init__(self, name: str, color: str, height: int=40):
        super().__init__(name, color, height)
        self._sound = 'Woof'

    def get_name(self):
        return self._name
    
    def get_color(self):
        return self._color
    
    def get_height(self):
        return self._height
    
    def voice(self):
        return self._sound
    
    @d.write_in_file_dec
    @d.func_time
    def move(self):
        time.sleep(int(self._speed()))

    def __add__(self, other):
        return Dog('puppy', other._color, height=5)
    
    def set_name(self, name: str):
        self._name = name

    def get_bigger(self):
        self._height += 20


class Cat(a.Animal):

    def __init__(self, name: str, color: str, height: int=20):
        super().__init__(name, color, height)
        self._sound = self.sound_calculate()

    def sound_calculate(self) -> str:
        if self._color == 'black':
            return 'Purr'
        else:
            return 'Meow'
        
    def get_name(self):
        return self._name
    
    def get_color(self):
        return self._color
    
    def get_height(self):
        return self._height
    
    def voice(self):
        return self._sound
    
    @d.write_in_file_dec
    @d.func_time
    def move(self):
        time.sleep(int(self._speed()))

    def __add__(self, other):
        return Cat('kitty', self._color, height=2)
    
    def set_name(self, name: str):
        self._name = name

    def get_bigger(self):
        self._height += 7


class Horse(a.Animal):

    def __init__(self, name: str, color: str, breed: str='Mustang', height: int=160):
        super().__init__(name, color, height, breed)
        self._sound = 'Neigh'
        self._speed = self.speed_calculate
        self._breed = breed

    def speed_calculate(self) -> int:
        if self._breed == 'Mustang':
            return 60
        else:
            return 55
        
    def get_name(self):
        return self._name
    
    def get_color(self):
        return self._color
    
    def get_height(self):
        return self._height
    
    def voice(self):
        return self._sound
    
    @d.write_in_file_dec
    @d.func_time
    def move(self):
        time.sleep(self._speed())

    def __add__(self, other):
        return Cat('foal', other._color, height=50)
    
    def set_name(self, name: str):
        self._name = name

    def get_bigger(self):
        self._height += 50    
    
        
    
