def nugzar_chubinidze(sadgerdzelo, limit):
  """
  ნუგზარ ჩუბინიძის სადღეგრძელოს ფუნქცია.

  Args:
    sadgerdzelo: დალეული ჭიქების რაოდენობა.
    limit: დასაშვები ჭიქების მაქსიმალური რაოდენობა.

  Returns:
    შეტყობინება იმის მიხედვით, გადააჭარბა თუ არა ნუგზარმა ლიმიტს.
  """
  if sadgerdzelo > limit:
    return "ლუიზა: ნუგზარი აღარ დალიო მეტი!"
  else:
    return "მოდი ახლა მართლა, დამილოცნიე"

# მაგალითები:
daleuli_raodenoba1 = 3
limiti1 = 5
shetyobineba1 = nugzar_chubinidze(daleuli_raodenoba1, limiti1)
print(f"ნუგზარს დალეული აქვს {daleuli_raodenoba1} ჭიქა, ლიმიტია {limiti1}. შეტყობინება: {shetyobineba1}")

daleuli_raodenoba2 = 7
limiti2 = 4
shetyobineba2 = nugzar_chubinidze(daleuli_raodenoba2, limiti2)
print(f"ნუგზარს დალეული აქვს {daleuli_raodenoba2} ჭიქა, ლიმიტია {limiti2}. შეტყობინება: {shetyobineba2}")



def yuri_gagarini():
  """
  ამოწმებს მომხმარებლის გულის წნევასა და პულსს იური გაგარინის მაჩვენებლებთან.

  Returns:
    True, თუ მომხმარებლის პულსი ემთხვევა იური გაგარინის პულსს (80),
    False, წინააღმდეგ შემთხვევაში.
  """
  try:
    gulis_tsneva = int(input("შეიყვანეთ თქვენი გულის წნევა: "))
    pulsi = int(input("შეიყვანეთ თქვენი პულსი: "))

    if pulsi == 80:
      return True
    else:
      return False
  except ValueError:
    print("გთხოვთ შეიყვანოთ რიცხვითი მნიშვნელობები.")
    return False

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
shedegi = yuri_gagarini()
print(shedegi)



def unikaluri_vashlebi(vashlebis_sia):
  """
  იღებს ვაშლების სიას და აბრუნებს სიას, სადაც მხოლოდ უნიკალური ვაშლებია დარჩენილი.

  Args:
    vashlebis_sia: ვაშლების სახელების სია (მაგ., ["პანტა", "პანტა", "გორული"]).

  Returns:
    ვაშლების სახელების სია უნიკალური ელემენტებით.
  """
  unikaluri_vashlebi_set = set(vashlebis_sia)
  unikaluri_vashlebi_sia = list(unikaluri_vashlebi_set)
  return unikaluri_vashlebi_sia

# მაგალითი გამოყენებისთვის
vashlebis_sia = ["პანტა", "პანტა", "გორული", "სტარკი", "პანტა", "რენეტი", "გორული"]
unikaluri_sia = unikaluri_vashlebi(vashlebis_sia)
print(f"საწყისი ვაშლების სია: {vashlebis_sia}")
print(f"უნიკალური ვაშლების სია: {unikaluri_sia}")