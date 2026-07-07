class Course:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print("Total Students =",cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18
student1=Course("Bobby")
student2=Course("Nani")
student3=Course("kumar")
student1.enroll()
student2.enroll()
student3.enroll()
Course.show_total()
print(Course.is_eligible(25))
print(Course.is_eligible(18))
print(Course.is_eligible(16))



