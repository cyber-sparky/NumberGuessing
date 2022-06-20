print("Think any number from 1 to 100")
print("------------------Lets Start-------------------")
print("Enter Y for Yes and N for No")
print("-----------------------------------------------")

middle=50
counter=8

def middlenumber(val):
    global counter
    global middle
    if val=='y' or val=='Y':
        if (counter==7):
            middle=middle+25
            return middle
        elif (counter==6):
            middle=middle+12
            return middle
        elif (counter==5):
            middle=middle+6
            return middle
        elif (counter==4):
            middle=middle+3
            return middle
        elif (counter==3):
            middle=middle+2
            return middle
        elif (counter==2):
            middle=middle+1
            return middle
        elif (counter==1):
            counter=0
            middle=middle+1
            return middle
    elif val=='n' or val=='N':
        if (counter==7):
            middle=middle-25
            return middle
        elif (counter==6):
            middle=middle-12
            return middle
        elif (counter==5):
            middle=middle-6
            return middle
        elif (counter==4):
            middle=middle-3
            return middle
        elif (counter==3):
            middle=middle-2
            return middle
        elif (counter==2):
            middle=middle-1
            return middle
        elif (counter==1):
            counter=0
            return middle
    else:
        print("Please enter your answers only in Y/N !!!")
        counter+=1
        return middle
            
while (counter!=0):
    counter-=1
    print("Is the number you think greater than %d?" %middle)
    value=input()
    middle=middlenumber(value)
    
print ("The number you think is %d" %middle)