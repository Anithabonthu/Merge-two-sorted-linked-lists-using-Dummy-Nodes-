#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
def RemoveDuplicates(list):
    stack=[]
    curr=list
    while curr:
        if curr.data not in stack:
            stack.append(curr.data)
            prev=curr
        else:
            prev.next=curr.next
        curr=curr.next
   
list1=LinkedList()
print("Enter Elements into List1.")
while True:
    print("1.Insertion  2.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        list1.insert(value)
    elif ch==2:            
        break
RemoveDuplicates(list1.head)
list1.print()


# In[ ]:





# In[ ]:




