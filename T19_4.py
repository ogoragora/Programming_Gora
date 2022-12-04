from abc import ABC

class Creature(ABC):
    name = ''
    def __init__(self, age, lifeSpan, growthMethod, feedingWay, supplyCapacity, speed, breedingConditions):
        self.age = age
        self.lifeSpan = lifeSpan
        self.growthMethod = growthMethod
        self.feedingWay = feedingWay
        self.supplyCapacity = supplyCapacity
        self.speed = speed
        self.breedingConditions = breedingConditions

    def update(self, time): 
        self.age += time
        if self.age > self.lifeSpan:
            self.age = self.lifeSpan

    def getState(self):
        if(self.age == self.lifeSpan):
            return self.name + ': ' + str(self.age) + ' - reached max life span, dead'
        return self.name + ': ' + str(self.age)
        

class Animal(Creature):
    pass

class Dog(Animal):
    name = 'dog'
    pass

class Fish(Animal):
    name = 'fish'
    pass

class Bird(Animal):
    name = 'bird'
    pass



class Herb(Creature):
    pass

class Potato(Herb):
    name = 'potato'
    pass

class Carrot(Herb):
    name = 'carrot'
    pass

class Blackberry(Herb):
    name = 'blackberry'
    pass


creaturesAmount = 6
T = 3
dog1 = Dog(6, 20, 'constant power supply', 'other creatures, food', 0.5, 50, 'moderate temperature')
fish = Fish(5, 12, 'constant power supply', 'other creatures, food', 0.2, 10, 'moderate temperature') 
dog2 = Dog(8, 18, 'constant power supply', 'vegetation, small invertebrates, zooplankton, zoobenthos and detritus', 0.4, 45, 'moderate temperature')
bird = Bird(9, 60, 'constant power supply', 'other creatures, food', 2, 80, 'moderate temperature')
potato = Potato(0.4, 1, 'constant power supply, availability of soil', 'nutrients, sun', 0, 0, 'the presence of tubers')
blackberry = Blackberry(0.1, 0.3, 'constant power supply', 'nutrients, sun', 0, 0, 'apical cuttings, seeds, lignified offspring, root and green cuttings')

creatures = [dog1, fish, dog2, bird, potato, blackberry]
for i in range(1, T + 1):
    print('\nAfter ' + str(i) + ' year:')
    for j in range(creaturesAmount):
        creatures[j].update(T)
        print(creatures[j].getState())
