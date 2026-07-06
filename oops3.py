class mathops:
    @staticmethod
    def is_even(num):
        return num%2==0
ob=mathops()
print(ob.is_even(8))
print(mathops.is_even(7))