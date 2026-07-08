class Student:
    total_students=0
    passing_marks=35
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_students+=1
    def result(self):
        if self.marks>=Student.passing_marks:
            return "Passed"
        else:
            return "Failed"
    @classmethod
    def curve_marks(cls,students,percentage):
        for student in students:
            student.marks+=student.marks*(percentage/100)
            if student.marks>100:
                student.marks=100
    @staticmethod
    def grade(marks):
        if marks>90:
            return "A"
        elif marks>80:
            return "B"
        elif marks>70:
            return "C"
        elif marks>50:
            return "D"
        elif marks>=Student.passing_marks:
            return "E"
        else:
            return "F"
    def display(self):
        print("NAME:",self.name)
        print("MARKS:",self.marks)
        print("GRADE:",Student.grade(self.marks))
        print("RESULT:",self.result())
s1=Student("ROY",50)
s2=Student("UMA",75)
s3=Student("PAVAN",80)
print("TOTAL STUDENTS:",Student.total_students)
students=[s1,s2,s3]
print("BEFORE APPLYING CURVE MARKS:")
for student in students:
    student.display()
Student.curve_marks(students,10)
print("AFTER APPLYING 10% CURVE MARKS:")
for student in students:
    student.display()

