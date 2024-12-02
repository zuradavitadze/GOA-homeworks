number = int(input("შეიყვანეთ რიცხვი: "))

if number % 2 == 0:
    print(number, "არის ლუწი რიცხვი")
else:
    print(number, "არის კენტი რიცხვი")

for i in range(1, 101):
    if i % 2 == 0:
        print(i, "არის ლუწი რიცხვი")
    else:
        print(i, "არის კენტი რიცხვი")