class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=Student.passing_marks:
            print(f"{self.name}: Pass")
        else:
            print(f"{self.name}: Fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
        print("Passing Marks updated to:",cls.passing_marks)
    @staticmethod
    def grade_category(marks):
        if marks>=90:
            return "A"
        elif marks>=75:
            return "B"
        else:
            return "C"
s1=Student("yash",35)
s2=Student("jacob",80)
s3=Student("kumar",90)
print(f"Initial passing Marks:{Student.passing_marks}")
print("Student Details:")
print(s1.name,"- Grade:",s1.grade_category(s1.marks))
s1.result()
print(s2.name,"- Grade:",s2.grade_category(s2.marks))
s2.result()
print(s3.name,"- Grade:",s3.grade_category(s3.marks))
s3.result()
Student.update_passing_marks(35)
print("Result After Update Passing Marks:")
print(s1.name,"- Grade:",Student.grade_category(s1.marks))
s1.result()
print(s2.name,"- Grade:",s2.grade_category(s2.marks))
s2.result()
print(s3.name,"- Grade:",s3.grade_category(s3.marks))
s3.result()