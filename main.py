from glob import glob
import sys

from django.conf import UserSettingsHolder
from database import Item, User, UserItems, session

# Main app function
def main():
  try:
    print(" ctrl + c : exit the program ")
    registerOrloggin()
  except KeyboardInterrupt:
    sys.exit("\n\n     Existing ....")
    
    
def todo_app():
    from sqlalchemy.exc import IntegrityError
    while True:
    
        print(f"\n       Hello {username}  \U0001F642    ")        
        print()
        print("\nWhat do you want to do today?")
        print("1: View todo items")
        print("2: Create new todo item")
        print("3: Remove item")
        print("4: Switch User")
        print("5: log out")
        print("6: Exit the program\n")
        selection = input()
        if (selection == "1"): showItems()
        elif (selection == "2"):
            try:
                createItem()
                addTouseritems(username) 
            except IntegrityError:
                sys.exit("existing...Integrity Error Occur!")

        elif (selection == "3"): removeItem(username)
        elif (selection =="4"):  switchUser()
        elif (selection =="5"):  tologgout()
        elif (selection == "6"):
          sys.exit("existing...")
        


# Lists all todo items
def showItems():
  print("\nYour todo lists:")
  print("---")
  user=session.query(User).filter(User.userId== getuserId()).first()
  counter=0
  for item in user.items:
    counter+=1
    print(counter ,". Id :",item.itemId,",",item.name)
    #print(item.itemId, ": " + item.name)
  print("---\n")
  session.commit()
    
            

# Creates new todo item
def createItem():
  global items
  global itemName
  print("Name for the item:")
  itemName = input()
  newItem = Item(name = itemName)
  session.add(newItem)
  session.commit()
  

# Removes todo item with ID
def removeItem(username):
  from sqlalchemy.orm.exc import NoResultFound
  #get associated user's Id
  user_item_ids=[]
  user=session.query(User).filter(User.userId== getuserId()).first()
  for item in user.items:
    user_item_ids.append(item.itemId)
  try:
    itemId = int(input())
    if itemId in user_item_ids:
      removableItem = session.query(Item).filter(Item.itemId == itemId)
      session.delete(removableItem.one())
      session.commit()
    else:
      print("Invalid Id ")
  except  ValueError as e:
    print(e)
  except NoResultFound:
    print("No resultFound") 
  except itemId not in user_item_ids:
    print("No resultFound")
  except itemId not in user_item_ids:
    print("No resultFound")

            

def toRegistor():
  
  print("        ---------------------------------")
  print("       |      Registoring for Users      |")
  print("        ---------------------------------")
  username =input("Enter your Username: ")
  email = input("Enter your email: ")
  password =input("Enter your Password: ")
  
  user_=session.query(User).filter((User.username ==username) | (User.email ==email)).first()
  if user_ is not None:
    if user_.username==username:
      print("User name already exits!")
      print("Try again !")
      toRegistor()
    elif user_.email==email:
      print("User email already exits!")
      print("Try again !")
      toRegistor()
  else:
    session.add(User(
          username=username,
          email=email,
          password=password
      ))
    session.commit()
    user_=session.query(User).filter((User.username ==username) | (User.email ==email)).first()
    print("        --------------------------------")
    print("       |    User created successfully   |")
    print("        --------------------------------")
    while True:
      print("\n")
      print("1: To Registor New user")
      print("2: To Login")
      print("3: To exit the program")
      user_choice=input()
      if (user_choice == "1"): toRegistor()
      if (user_choice=="2"): toLogin() 
      elif (user_choice == "3"): sys.exit("Goodbye!")
      else:
        continue
    
 
  
def toLogin():
  print("        ------------------------------")
  print("       |      Log  in for Users       |")
  print("        ------------------------------")
  global username
  username =input("Enter your Username: ")
  password =input("Enter your Password: ")
  user=session.query(User).filter(User.username ==username).first()
  user_pass=session.query(User).filter(User.password ==password).first()
  if user is not None and user_pass is not None:
    todo_app()
  else:
    print("      ---------------------------------------")
    print("     |    Username or Password Incorrect!    |")
    print("      ---------------------------------------")
    print("\tCreate your account or Try logging in again!")
    registerOrloggin()
    

def registerOrloggin():
    print("        ------------------------------")
    print("       |      Registor or Log In      |")
    print("        ------------------------------")
    while True:
      try:
        user_input=int(input("        Press 0 to registor and press 1 to login : "))
        if user_input==0:
          toRegistor()
          break
        elif user_input==1:
          toLogin() 
          break
        else:
          registerOrloggin()
      except ValueError:
        print("\n\n\t\t\tinvalid input ! \n\t\t\tPlease Try agian!\n")
        registerOrloggin()
        

def getuserId():
  global username
  user_id=session.query(User).filter(User.username==username).first()
  return user_id.userId

# def getitemId():
#   print("get item id ")
#   items_id=[]
#   items= session.query(Item)
#   for item in items:
#     items_id.append(item.itemId)
#     return items_id

def addTouseritems(username):
  print("adding data to associated table...")
  user_id=session.query(User).filter(User.username==username).first()
  userId=user_id.userId
  item_Id= session.query(Item).filter(Item.name==itemName).first()
  session.add(UserItems(userId=userId,itemId=item_Id.itemId))
  session.commit()

def switchUser():
  toLogin()

def tologgout():
  registerOrloggin()


# Start the app
if __name__ == "__main__":
  print("       Welcome to TOD-O LIST O-MAKER Version 5123.524     \n")
  main()