from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        pass

    def add_robot(self,robots):
        self.robots.append(robots)

    robot_one = Robot("Prime")
    robot_two = Robot("Lazer")
    robot_three = Robot("Axle")

    