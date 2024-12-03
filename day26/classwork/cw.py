import turtle

def walk():
  turtle.forward(200)
  turtle.left(90)
  turtle.backward(200)
  turtle.right(90)

def fal_back():
  turtle.right(180)

def combined_action():
  walk()
  fal_back()

# ფუნქციის გამოძახება:
combined_action()
