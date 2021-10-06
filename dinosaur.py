

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        self.health.robot = self.attack_power - self.health.robot 
        print(f"Successful hit on {robot}! Health reduced to: {self.health.robot}")

    