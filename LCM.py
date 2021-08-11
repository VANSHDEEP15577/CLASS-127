num1=int(input("ENTER THE FIRST NUMBER:"))
num2=int(input("ENTER THE SECOND NUMBER:"))
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if lcm%num1==0 and lcm%num2==0:
        break
    else:
        lcm+=1
print("LCM IS ",lcm)