class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f'{self.name} летает')

    def eat(self):
        print(f'{self.name} питается')

    def sing(self):
        print(f'{self.name} поет - voice1')
    def info(self):
        print(f'{self.name} - имя')
        print(f'{self.voice} - голос')
        print(f'{self.color} - окрас')

class Pigeon(Bird):
    def __init__(self,name,voice,color,ffood):
        super().__init__(name,voice,color)
        self.ffood = ffood
    pass
    def walk(self):
        print(f'{self.name} walk - roam')
    def sing(self):
        print(f'{self.name} sing - voice2')

bird1 = Pigeon('Гоша','voice','gray','crumbs')
bird2 = Bird('Паша','voice','gray')

bird1.sing()
bird1.info()
bird1.walk()
bird2.sing()