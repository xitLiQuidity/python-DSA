class Node:
    def __init__(self,data):
        self.data = data 
        self.addr = None
    
class Single_Linked_List:
    def __init__(self):
        self.head= None

    def insert_at_last(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.addr != None:
                temp = temp.addr
            temp.addr = newNode

    def display(self):
        if self.head is None:
            print("No nodes to display")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" -> ")
                temp = temp.addr
            print()

    def lenght(self):
        if self.head is None:
            print("No nodes to count")
        else:
            temp = self.head
            cnt = 0 
            while temp:
                cnt += 1 
                temp = temp.addr
            return cnt
    
    def insert_at_first(self,val):
         newNode = Node(val)
         if self.head is None:
              self.head = newNode
         else:
              newNode.addr = self.head
              self.head = newNode


s1 = Single_Linked_List()
s1.insert_at_last(10)
s1.insert_at_last(20)
s1.insert_at_last(30)
s1.display()
print("total nodes in SSl ->", s1.lenght())
