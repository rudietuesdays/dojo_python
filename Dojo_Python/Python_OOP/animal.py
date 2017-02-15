#create a class called 'Animal' with attributes name and health
class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    #give Animal the following methods: walk, run, displayHealth
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Name:",  self.name
        print "Health:", self.health

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

animal1 = Animal("panda")

animal1.walk().walk().walk().run().run().displayHealth()

dog1 = Dog("Rover")

dog1.walk().walk().walk().run().run().pet().displayHealth()

dragon1 = Dragon("Pete")

dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()

# test out fly and pet to make sure they don't work
# animal1.fly().displayHealth()
# animal1.pet().displayHealth()
