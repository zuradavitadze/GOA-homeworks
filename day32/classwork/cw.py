def no_space(x):
  return x.replace(" ", "")
def no_space(x):
  return "".join(x.split())
def no_space(x):
  result = ""
  for char in x:
    if char != " ":
      result += char
  return result