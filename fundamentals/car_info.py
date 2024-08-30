class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def dispay_info(self):
        print(f"Car Information:{self.year} {self.make}{self.model}")

my_car = Car("BMW","F10 m5", 2024)

my_car.dispay_info()