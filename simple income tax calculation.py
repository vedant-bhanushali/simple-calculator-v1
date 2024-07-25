print("                                            ")

print("THIS IS A SIMPLE INCOME TAX CALCULATOR BASED ON NEW BUDGET OF JULY 2024 OF INDIA")



salary = float(input("Enter your annual salary: "))
#
if (salary >= 300000):
    tax1 = (salary * (0.05))
    print(tax1)


elif (salary <= 300000) :
    print("tax = 0")

#

if (salary >= 700000) :
    tax2 = (salary * (0.10))
    print(tax2)

elif (salary <= 700000) :
    print(tax1)
