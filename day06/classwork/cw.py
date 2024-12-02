name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")

full_name = name + " " + surname
print("თქვენი სრული სახელია:", full_name)

name1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
name2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
operator = input("შეიყვანეთ ოპერატორი (+, -, //, /, *, **): ")

if operator == "+":
    result = name1 + name2
elif operator == "-":
    result = name1 - name2
elif operator == "//":
    result = name1 // name2
elif operator == "/":
    result = name1 / name2
elif operator == "*":
    result = name1 * name2
elif operator == "**":
    result = name1 ** name2
else:
    print("არასწორი ოპერატორი")

print("შედეგი:", result)