class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
        
class Llist:
    def __init__(self):
        self.head= None
        
    def printList(self):
        temp= self.head
        
        while(temp):
            print(temp.data)
            temp= temp.next 
            
            
    def push(self,data):
        
        newnode= Node(data)
        newnode.next= self.head
        self.head= newnode
        
    def append(self,data):
        
        newnode= Node(data)
        
        if self.head==None:
            
            self.head =newnode
            return
        
        
        temp= self.head
        while temp.next :
            
            temp= temp.next
            
        temp.next= newnode
        
    
    def insertAfter(self,prev,data):
        
        newnode= Node(data)
        
        newnode.next= prev.next
        prev.next= newnode
        
    def pop(self):
        
        if self.head==None:
            return None

        temp= self.head
        self.head= self.head.next
        temp=None
        
    def deleteEnd(self):
        
        if self.head==None:
            self.head=None
            return
        
        temp = self.head
        
        while temp.next:
            prev= temp
            temp= temp.next
            
        prev.next= None
        temp= None
        
     
    
        
    def deleteKey(self,key):
        
        if self.head==None:
            return None
        
        temp= self.head
        
        if temp.data==key:
            self.head= self.head.next
            temp= None
            
            
            return
        
        while temp.next:
            
            if temp.data==key:
                break
            
            prev= temp
            temp= temp.next
            
        prev.next=temp.next
        temp= None
            
            
            
        
        
        
        
        
            
            
            
        
        
            
                       
        
llist= Llist()

llist.head= Node(1)
second= Node(2)
third= Node(3)

llist.head.next= second
second.next= third
llist.push(9)
llist.push(7)
llist.push(89)

llist.append(8)
llist.insertAfter(llist.head,99)
llist.pop()
llist.deleteKey(3)
llist.deleteEnd()
llist.printList()


