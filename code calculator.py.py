print("welcome to AOS vedant's calculator v1 ")

print("see the option and select the number when asked")

print("Multiply : 1")
print("Divide : 2")
print("Add : 3")
print("Subtract : 4 ")
print("power : 5")

choose = (input("choose the option from above (1,2,3,4,5) :"))
print ("made by aos vedant")

print("select the number 1 & 2 of your operation")

num1 = int(input("number 1 :"))
num2 = int(input("number 2 :"))


if( choose == "1"):
    print("THE ANSWER :" , num1 * num2)



elif( choose == "2"):
    print("THE ANSWER :" , num1 / num2)



elif( choose == "3"):
    print("THE ANSWER :" , num1 + num2)



elif( choose == "4"):
    print("THE ANSWER :" , num1 - num2)

elif( choose == "5") :
    print("THE ANSWER :" , num1 ** num2)

else :
    print("wrong option choosen TRY AGAIN")

print (" Thank you for using aos calculator")
print ("made by aos vedant")
