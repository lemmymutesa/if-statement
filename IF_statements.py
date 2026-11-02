#accept input
amount= float(input("enter amount: "))
member = input("are you a member? (yes/no): ")

#chech whether a member or not 
if amount >= 1000:
    if member == "yes":
        discount = amount * 0.2
        print("Discount =", discount)
    else:
        discount = amount * 0.1
        print("Discount =", discount)
else:
    print("No discount")