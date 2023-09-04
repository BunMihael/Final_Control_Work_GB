from animal import Animal, DomesticAnimal, BeastOfBurden

class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_all_animals(self):
        return self.animals

    def find_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None
