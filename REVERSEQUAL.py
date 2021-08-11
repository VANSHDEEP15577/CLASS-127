num=int(input("ENTER THE NUMBER:"))
rev=0
org=num
while num>0:
    rem=num%10
    rev=rem+(rev*10)
    num=int(num/10)
if org==rev:
    print("THE NUMBER IS EQUAL")
else:
    print("THE NUMBER IS NOT EQUAL")