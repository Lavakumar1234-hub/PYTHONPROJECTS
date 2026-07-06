class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print(f"mileage={self.mileage}")
        print(f"wheels={self.wheels}")
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
ob=Car(50)
print("Before wheels Change:")
ob.display_specs()
Car.change_wheels(6)
print("After Wheels Change:")
ob.display_specs()