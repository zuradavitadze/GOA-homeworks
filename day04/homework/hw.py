name = input("შეიყვანეთ თქვენი სახელი: ")
last_name = input("შეიყვანეთ თქვენი გვარი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

print(name, last_name, "არის", age, "წლის")

first = int(input("შეიყვანეთ პირველი რიცხვი: "))
second = int(input("შეიყვანეთ მეორე რიცხვი: "))

sum = first + second
difference = first - second
quotient = first / second
product = first * second

print("ჯამი:", sum)
print("სხვაობა:", difference)
print("განაყოფი:", quotient)
print("ნამრავლი:", product)

math = 20 + int("20")
math = math - 10
math = math * 2
print(math)