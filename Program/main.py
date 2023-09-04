from animal import Animal, DomesticAnimal, BeastOfBurden
from registry import AnimalRegistry

def main():
    registry = AnimalRegistry()

    while True:
        print("\n--- Menu ---")
        print("1. Add animal")
        print("2. Show commands of animal")
        print("3. Teach animal a new command")
        print("4. List all animals")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter animal's name: ")
            birth_date = input("Enter animal's birth date (YYYY-MM-DD, for example, 2022-05-01): ")
            animal_type = input("Is it a Domestic animal or Beast of burden? (D/B): ")

            if animal_type.lower() == "d":
                fur_type = input("Enter fur type: ")
                command = input("Enter command it can perform: ")
                animal = DomesticAnimal(name, birth_date, command, fur_type)
            elif animal_type.lower() == "b":
                command = input("Enter command it can perform: ")
                load_capacity = float(input("Enter its load capacity: "))
                animal = BeastOfBurden(name, birth_date, command, load_capacity)

            registry.add_animal(animal)
            print(f"{name} has been added to the registry!")

        elif choice == "2":
            name = input("Enter animal's name: ")
            animal = registry.find_animal(name)
            if animal:
                animal.perform_command()
            else:
                print(f"No animal named {name} found in the registry.")

        elif choice == "3":
            name = input("Enter animal's name: ")
            animal = registry.find_animal(name)
            if animal:
                new_command = input("Enter a new command for the animal: ")
                animal.teach_new_command(new_command)
            else:
                print(f"No animal named {name} found in the registry.")

        elif choice == "4":
            animals = registry.list_all_animals()
            if animals:
                for a in animals:
                    print(a)
            else:
                print("No animals in the registry yet.")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
