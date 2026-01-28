name = input ("Please enter your name: ")
age = int (input ("Please enter your age: "))
email = input ("Please enter your email: ")
mobile = input ("Please enter your mobile number: ")
valid =True
if len(name)==0 :
    valid =False
elif name[0]==" " or name[len(name)-1]==" " :
    valid = False
elif name.count(" ")<1 :
    valid = False

if email.count("@")!=1 or email.count(".")< 1 :
     valid =False
elif email[0]=="@":
     valid =False

if len(mobile)!= 10:
    valid =False
elif mobile.isdigit() == 0 :
    valid =False
elif mobile[0]=="0" :
    valid =False

if age<18 or age>60 :
    valid =False

if valid == True :
    print ("User Profile is VALID")
else :
    print ("User Profile is INVALID")