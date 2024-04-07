def get_item(x):

  if x == 1:
    print("Cheeseburger")
  elif x == 2:
    print("Fries")
  elif x == 3:
    print("Soda")
  elif x == 4:
    print('Ice cream')
  elif x == 5:
    print("Cookie & Cream")
  else:
    return "Only 5 on the table not more!"
    
def welcome():
  print("Welcome to hamburger button! Can I tell you what's here tonight!")
  print("Glad to have you here today's menu is ")
  print("1 is Cheeseburger")
  print("2 is Fries")
  print("3 is Soda")
  print("4 is Icecream")
  print("5 is Cookie")

welcome()

option = int(input("Can you please tell me your order? "))
print(get_item(option))