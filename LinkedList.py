from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    #Adds a node at front
    def append(self, new_contact):
        if(self.head):
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next

            pointer.next = Node(new_contact)
        else:
            self.head = Node(new_contact)

        self.size += 1
    #Print phone book
    def print(self):
        print("Phone Book:")
        if(self.size == 0):
            print("EMPTY")
        index = 0
        head = self.head
        #Iters list
        while (self.head):
            print(f'[{index}] {self.head.contact.name} - {self.head.contact._number}')
            index += 1
            self.head = self.head.next
        #Set head to original head
        self.head = head


    def remove_by_name(self, name):
        if(self.size > 0):
            head = self.head
            prev = head
            is_in = False

            if(self.head.contact.name.lower().strip() == name.lower().strip()):
                self.head = self.head.next
                is_in = True

            else:
                while(self.head):
                    if(self.head.contact.name.lower().strip() == name.lower().strip()):
                        prev.next = self.head.next
                        self.head = prev
                        is_in = True
                    prev = self.head
                    self.head = self.head.next

                self.head = head

            if(not is_in):
                print("Name not found")

        else:
            print("List has no contacts to be removed")

    def remove_by_id(self, id):
        if(self.size > 0):
            counter = 0
            head = self.head
            prev = head

            if(self.size > id):
            
                if(counter == id):
                    self.head = self.head.next
                
                else:
                    while(counter <= id):
                        if(counter == id):
                            prev.next = self.head.next
                            self.head = prev
                        counter += 1
                        prev = self.head
                        self.head = self.head.next
                    self.head = head
            else:
                print("Invalid Value")
        
        else:
            print("List has no contacts to be removed")