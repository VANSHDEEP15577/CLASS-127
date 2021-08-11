num1=int(input("ENTER THE FIRST NUMBER:"))
num2=int(input("ENTER THE SECOND NUMBER:"))
if num1>num2:
    hcf=num1
else:
    hcf=num2
while True:
    if hcf%num1==0 and hcf%num2==0:
        break
    else:
        hcf-=1
print("HCF IS ",hcf)