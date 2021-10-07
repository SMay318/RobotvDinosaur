from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur_one = Dinosaur("Rex", 10)
        dinosaur_two = Dinosaur("Rampage", 15)
        dinosaur_three = Dinosaur("Godzilla", 20)
        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)
        


    