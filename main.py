from Contact import Contact
from LinkedList import LinkedList
from Node import Node
import os

if __name__ == "__main__":
    aux = -1
    new_list = LinkedList()

    while(aux != 0):
        aux = int(input("1 - Add contact\n2 - Delete contact by name\n3 - Delete contact by index\n4 - Show Phone Book\n0 - Exit\n"))

        if(aux == 1):
            os.system('cls' if os.name == 'nt' else 'clear')
            name = input("Insert name: ")
            number = int(input("Insert number: "))
            new_list.append(Contact(number, name))
            os.system('cls' if os.name == 'nt' else 'clear')

        elif(aux == 2):
            name = input("Insert name to be deleted: ")
            new_list.remove_by_name(name)
        elif(aux == 3):
            new_list.print()
            id = int(input("Insert ID to be deleted: "))
            new_list.remove_by_id(id)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif(aux == 4):
            os.system('cls' if os.name == 'nt' else 'clear')
            new_list.print()

        elif(aux == 0):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Goodbye!")

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Wrong value")

