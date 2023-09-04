class Animal:
    def __init__(self, name, birth_date, command):
        self.name = name
        self.birth_date = birth_date
        self.command = command

    def perform_command(self):
        print(f"{self.name} performs the command: {self.command}")

    def teach_new_command(self, new_command):
        self.command = new_command
        print(f"{self.name} has learned a new command: {self.command}")

    def __str__(self):
        return f"Name: {self.name}, Birth Date: {self.birth_date}, Command: {self.command}"

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date, command, fur_type):
        super().__init__(name, birth_date, command)
        self.fur_type = fur_type

    def __str__(self):
        return f"Name: {self.name}, Type: Domestic, Birth Date: {self.birth_date}, Command: {self.command}, Fur Type: {self.fur_type}"

class BeastOfBurden(Animal):
    def __init__(self, name, birth_date, command, load_capacity):
        super().__init__(name, birth_date, command)
        self.load_capacity = load_capacity

    def __str__(self):
        return f"Name: {self.name}, Type: Beast of Burden, Birth Date: {self.birth_date}, Command: {self.command}, Load Capacity: {self.load_capacity}"
