# Superclass for Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type 

# Subclass for Automobile which inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
      
        super().__init__("car")  # Setting the vehicle type as car
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        # Display the details of the car 
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# user input
def main():
    print("Welcome to the Car Information App")

    # Getting user input for car details
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

   
    car = Automobile(year, make, model, doors, roof)

    # Displaying the car details
    car.display_info()

if __name__ == "__main__":
    main()
