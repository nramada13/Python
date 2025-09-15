## Noor Ramadan
## Module 3 Lab
## This program defines a Vehicle superclass and an Automobile subclass.

# Superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass Automobile inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")   # Vehicle type is always car
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("\nVehicle Information:")
        print(f"  Vehicle type: {self.vehicle_type}")
        print(f"  Year: {self.year}")
        print(f"  Make: {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Number of doors: {self.doors}")
        print(f"  Type of roof: {self.roof}")


# -------- Main --------
def main():
    # Collect user input
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter number of doors (2 or 4): ")
    roof = input("Enter type of roof (solid or sun roof): ")

    # Create an Automobile object with the user input
    car = Automobile(year, make, model, doors, roof)

    # Output the information
    car.display_info()


if __name__ == "__main__":
    main()

