class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal>0
Employee1=Employee("Kumar",50000)
Employee2=Employee("Siva",40000)
print("Before Bonus update:")
print(Employee1.name,"Final Salary:",Employee1.base_salary)
print(Employee2.name,"Final salary:",Employee2.base_salary)
Employee.update_bonus(0.2)
print("After Bonus update:")
print(Employee1.name,"Final salary:",Employee1.final_salary())
print(Employee2.name,"Final salary:",Employee2.final_salary())