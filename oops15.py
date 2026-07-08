class Course:
    total_courses=0
    min_duration=1
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
        self.enrolled_students=[]
        Course.total_courses+=1
    def enroll_students(self,student):
        self.enrolled_students.append(student)
    def is_valid_duration(self):
        return self.duration >= Course.min_duration and Course.is_realistic_duration(self.duration)
    @classmethod
    def updating_min_duration(cls,new_duration):
        cls.min_duration=new_duration
    @staticmethod
    def is_realistic_duration(duration):
        return 0<=duration<=50
    def display(self):
        print("TITLE:",self.title)
        print("DURATION:",self.duration,"WEEKS")
        print("ENROLLED STUDENTS:",self.enrolled_students)
        print("VALID DURATION:",self.is_valid_duration())
        print()
s1=Course("PYTHON PROGRAMMING",10)
s2=Course("STRUCTURED QUERY LANGUAGE",4)
s3=Course("DATA STRUCTURES AND ALGORITHM",12)
print("TOTAL COURSES:",Course.total_courses)
print()
courses=[s1,s2,s3]
s1.enroll_students("KUMAR")
s1.enroll_students("GANESH")
s2.enroll_students("UMA")
s2.enroll_students("JAI")
s3.enroll_students("YASH")
s3.enroll_students("TARAK")
print("BEFORE UPDATING MINIMUM DURATION:")
print()
for course in courses:
    course.display()
Course.updating_min_duration(10)
print("AFTER UPDATING MINIMUM DURATION TO 10 WEEKS:")
print()
for course in courses:
    course.display()


