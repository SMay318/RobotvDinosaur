from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = 100
        self.weapon = Weapon()

    def attack(self, dinosaur):
        pass

    sword = Weapon("Sword", 10)
    axe = Weapon("Axe", 15)
    hammer = Weapon("Hammer", 20)