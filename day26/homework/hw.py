def draw_triangle(n):
  for i in range(n):
    print("*" * (2*i+1))

for i in range(1, 120, 2):  # იტერაცია კენტ რიცხვებზე 1-დან 119-მდე
  draw_triangle(i)
  if i % n == 0:  # თუ ინდექსი n-ზე იყოფა, მწვანედ შევღებავთ
    print("მწვანე სამკუთხედი")
  else:
    print("ლურჯი სამკუთხედი")


print("Hello, World!")


def even_or_odd(num):
  if num % 2 == 0:
    print("არ არის კენტი")
  else:
    print("კი არის კენტი")

even_or_odd(23)


import matplotlib.pyplot as plt

def draw_triangle(n):
  x = range(n)
  y = [0] * n
  plt.plot(x, y, 'o-')
  plt.show()

draw_triangle(10)

import turtle

t = turtle.Turtle()

for i in range(3):
  t.forward(100)
  t.left(120)

turtle.done()