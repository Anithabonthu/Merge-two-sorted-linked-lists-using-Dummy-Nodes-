#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
def swap(ptr1,ptr2):
    temp=ptr1.data
    ptr1.data=ptr2.data
    ptr2.data=temp
def Sorting(list1):          #Arranging the elements in descending order..
    swapped=True
    while swapped:
        swapped=False
        current=list1
        while current.next:
            if current.data<current.next.data:
                swap(current,current.next)
                swapped=True
            current=current.next
      
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
print("Before Sorting The Elements:")
list1.print() 
Sorting(list1.head)
print("After Sorting The Elements:")
list1.print() 


# In[ ]:




