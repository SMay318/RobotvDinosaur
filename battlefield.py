from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
       

    def run_game(self):
        print("Welcome to Robots vs Dinosaurs! You will choose to be the Dinosaurs or the Robots. Only one can be Victorious, choose wisely!")
        user_input = input("press 1 to be the Dinosaurs or 2 to be the Robots")
        if user_input == "1":
            print("Congrats you chose to be the Dinosaurs! Here is your herd:")
            herd_one = self.herd.create_herd()
            print(herd_one)
        elif user_input == "2":
            print("Congrats you chose to be the Robots! Here is your fleet:")
            fleet_one = self.fleet.create_fleet()
            print(fleet_one)

    def display_welcome(self):
        ## display who the user picked and then welcome to battle
        print(f"The battle is about to start, looks like you chose {}!")
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
        # print("current dinosaurs are left:")
        pass

    def show_robo_opponent_options(self):
        ## show robots health and who is left 
        # print("current robots are left:")
        pass
    
    def display_winner(self):
        # print("CONGRATULATIONS!!! YOU ARE THE WINNER!!!")
        ## whoever has no dinosaurs or robots left is the loser, then display winner!
        pass

    