#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        new=Node(value)
        if self.head is None:
            self.head=new
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            curr.next=new
    def print(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
def getDecimalValue(head):
    if head is None:
            return 0
    l=[]
    while head:
        l.append(str(head.data))
        head=head.next
    l="".join(l)
    return(int(l,2))
list1=LinkedList()
while True:
    print("1.Insertion  2.Traverse 3.exit" )
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        list1.insert(value)
    elif ch==2:            
        list1.print()
    elif ch==3:
        break
print("The decimal value of the number in the linked list is :",getDecimalValue(list1.head))


# In[ ]:




