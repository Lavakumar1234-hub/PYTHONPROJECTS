class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        return self.marks>40
student1=student("kumar",85)
student2=student("ram",90)
print(f"{student1.name} has {"passed" if student1.is_passed() else "Failed"}")
print(f"{student2.name} has {"passed" if student2.is_passed() else "failed"}")