class Member:
    bmi_limit=24
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def calculate_bmi(self):
        return self.weight/self.height**2
    def check_fit_status(self):
        bmi=self.calculate_bmi()
        if bmi <= Member.bmi_limit:
            return f"{self.name}: BMI={bmi:.2f} --> FIT"
        else:
            return f"{self.name}: BMI={bmi:.2f} --> NOT FIT"
    @classmethod
    def update_bmi_limit(cls,new_limit):
        cls.bmi_limit=new_limit
    @staticmethod
    def valid_inputs(height,weight):
        if isinstance(height,(int,float)) and isinstance(weight,(int,float)):
            if height>0 and weight>0:
                return True
        return False
member1=Member("VIRAT",1.65,75)
member2=Member("RONALDO",1.80,70)
member3=Member("MESSI",1.65,60)
print("BEFORE UPDATING BMI LIMIT:",Member.bmi_limit)
print()
print(member1.check_fit_status())
print(member2.check_fit_status())
print(member3.check_fit_status())
Member.update_bmi_limit(28)
print()
print("AFTER UPDATING BMI LIMIT:",Member.bmi_limit)
print()
print(member1.check_fit_status())
print(member2.check_fit_status())
print(member3.check_fit_status())
print()
print("INPUTS VALIDATION:")
print()
print("HEIGHT=1.65 AND WEIGHT=75:",Member.valid_inputs(1.65,75))
print("HEIGHT=-1.78 AND WEIGHT=80:",Member.valid_inputs(-1.78,80))
print("HEIGHT=1.80 AND WEIGHT=65:",Member.valid_inputs(1.80,65))








