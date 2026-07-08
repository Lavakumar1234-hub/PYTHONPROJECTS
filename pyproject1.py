import random
Alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G''H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers=['0','1','2','3','4','5','6','7','8','9']
Symbols=['!','@','#','$','%','&','*','(',')']
print("WELCOME TO THE PASSWORD GENERATOR:")
Alphabets_input=int(input("HOW MANY ALPHABETS WOULD HAVE IN YOUR PASSWORD:"))
Numbers_input=int(input("HOW MANY NUMBERS WOULD HAVE IN YOUR PASSWORD:"))
Symbols_input=int(input("HOW MANY SYMBOLS WOULD HAVE IN YOUR PASSWORD:"))
password_list=[]
for i in range(Alphabets_input):
    char=random.choice(Alphabets)
    password_list+=char
for i in range(Numbers_input):
    char=random.choice(Numbers)
    password_list+=char
for i in range(Symbols_input):
    char=random.choice(Symbols)
    password_list+=char
#print(password_list)
random.shuffle(password_list)
#print(password_list)
password=""
for i in password_list:
    password+=i
print("HERE YOUR PASSWORD:",password)