from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.robot_one = self.fleet.robots[0]
        self.robot_two = self.fleet.robots[1]
        self.robot_three = self.fleet.robots[2]

        self.herd = Herd()
        self.dinosaur_one = self.herd.dinosaurs[0]
        self.dinosaur_two = self.herd.dinosaurs[1]
        self.dinosaur_three = self.herd.dinosaurs[2]

    def run_game(self):
        if len(self.herd.dinosaurs) == 3 and len(self.fleet.robots) == 3:
            self.display_welcome()
        

        pass
        
            
    def display_welcome(self):
        ## display who the user picked and then welcome to battle
        print("Welcome to Robots vs Dinosaurs! You will be the Dinosaurs and fight against the Robots. Only one can be Victorious!")
        pass 
    
    def battle(self):
        ## display battle has begun
        #input("Press 1 to begin battle")
        pass

    def dino_turn(self, dinosaur):
        ## dinosaurs attacks robots 
        user_input = input("press 1 to attack robots")
        if user_input == "1": 
            self.herd_one[0].attack + fleet_one[0]
            self.herd_one[1].attack + fleet_one[1]
            self.herd_one[2].attack + fleet_one[2]
        ## return the health of the robots after they are attacked
            pass

    def robo_turn(self,robot):
        ## robot attacks dinosaurs
        user_input = input("press 1 to attack dnosaurs")
        if user_input == "1":
            self.fleet_one[0].attack + herd_one[0]
            self.fleet_one[1].attack + herd_one[1]
            self.fleet_one[2].attack + herd_one[2]
        ## return health of dinosaurs

            pass

    def show_dino_opponent_options(self):
        ## show dinosaurs health and who is left
        
        pass

    def show_robo_opponent_options(self):
        ## show robots health and who is left 
        
        pass
    
    def display_winner(self):
        # print("CONGRATULATIONS!!! YOU ARE THE WINNER!!!")
        ## whoever has no dinosaurs or robots left is the loser, then display winner!
        pass

    