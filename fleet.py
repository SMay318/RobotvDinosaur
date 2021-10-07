from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()


    def create_fleet(self):
        robot_one = Robot("Prime")
        robot_two = Robot("Lazer")
        robot_three = Robot("Axle")
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)
        

    

  

    