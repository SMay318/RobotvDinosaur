from dinosaur import Dinosaur
from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon()

    def attack(self, dinosaur):
        self.weapon - self.health.dinosaur = self.health.dinosaur
        print(f"Successful hit on {dinosaur}! Health reduced to: {self.health.dinosaur}")

    sword = Weapon("Sword", 10)
    axe = Weapon("Axe", 15)
    hammer = Weapon("Hammer", 20)