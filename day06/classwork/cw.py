name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")

full_name = name + " " + surname
print("თქვენი სრული სახელია:", full_name)


num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
operator = input("შეიყვანეთ ოპერატორი (+, -, *, /, //, **): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "//":
    result = num1 // num2
elif operator == "**":
    result = num1 ** num2
else:
    print("არასწორი ოპერატორი")

print("შედეგი:", result)



