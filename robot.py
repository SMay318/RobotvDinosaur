from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("sword", 10)

    def attack(self, dinosaur):
        self.health.dinosaur = self.weapon - self.health.dinosaur 
        print(f"Successful hit on {dinosaur}! Health reduced to: {self.health.dinosaur}")

