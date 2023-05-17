class Animal:

    def __init__(self, name: str, color: str, height: int=50, breed: str=None):
        self.name = name
        self.color = color
        self.height = height
        self.breed = breed
        self._sound = 'I dont know who i am'
        self.speed = self.speed_calculate()

    def voice(self):
        return self._sound
    
    def speed_calculate(self) -> int:
        if self.height <= 20:
            return 13
        else:
            return 17



class Dog(Animal):

    def __init__(self, name: str, color: str):
        super().__init__(name, color, height=40)
        self._sound = 'Woof'
    

class Cat(Animal):

    def __init__(self, name: str, color: str):
        super().__init__(name, color, height=20)
        self._sound = self.sound_calculate()

    def sound_calculate(self) -> str:
        if self.color == 'black':
            return 'Purr'
        else:
            return 'Meow'


class Horse(Animal):

    def __init__(self, name: str, color: str, breed: str='Mustang', height: int=160):
        super().__init__(name, color, height, breed)
        self._sound = 'Neigh'
        self.speed = self.speed_calculate()

    def speed_calculate(self) -> int:
        if self.breed == 'Mustang':
            return 60
        else:
            return 55

animal = Animal('Lucy', 'white')
cat = Cat('Tim', 'black')
another_cat = Cat('Sam', 'ginger')
dog = Dog('Ludwig', 'brown')
horse = Horse('Annabel', 'ginger', 'Brumby')
another_horse = Horse('Dany', 'brown', height=170)

animals = [animal, cat, another_cat, dog, horse, another_horse]
for animal_el in animals:
    print(f'I am {animal_el.name}. {animal_el.voice()}. My height is {animal_el.height} cm and my speed is {animal_el.speed} kmph')
