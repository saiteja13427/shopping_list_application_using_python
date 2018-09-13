import os
import time
shopping_list = []
def clear_screen():
     os.system("cls" if os.name =="nt" else "clear")

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to remove any item
""")

def remove_item():
    what_to_remove = input("What do you want to remove? ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
         print("enter an item which is there in the list")

    show_list()
def add_to_list(item):
    shopping_list.append(new_item)
    print("Added! List has {} items.".format(len(shopping_list)))


def show_list():
    clear_screen()
    print("Here's your list:")
    if len(shopping_list)==1:
        print("you have 1 item in your list")
    else:
        print("you have {} items in your list".format(len(shopping_list)))
    for item in shopping_list:
        print(item)
        time.sleep(0.5)


show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper()=="REMOVE":
        remove_item()
    else:
        add_to_list(new_item)

show_list()