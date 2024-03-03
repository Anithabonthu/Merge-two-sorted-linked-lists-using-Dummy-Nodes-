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
def MergingTwoSortedList(list1,list2):     #Merging the two sorted lists into one list 
    temp=ptr=Node(0)
    while list1  and list2:
        if list1.data<=list2.data:
            temp.next=list1
            temp=temp.next
            list1=list1.next
        else:
            temp.next=list2
            temp=temp.next
            list2=list2.next
    if list1 == None:
        while(list2):
            temp.next=list2
            temp=temp.next
            list2=list2.next
    else:
        while(list1):
            temp.next=list1
            temp=temp.next
            list1=list1.next
    return ptr.next
            
list1=LinkedList()
print("Enter Elements into List1.")
while True:
    print("1.Insertion  2.Traverse  3.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        list1.insert(value)
    elif ch==2:            
        list1.print()
    elif ch==3:
        break
list2=LinkedList()
print("Enter Elements into List2.")
while True:
    print("1.Insertion  2.Traverse  3.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        list2.insert(value)
    elif ch==2:
        list2.print()
    elif ch==3:
        break

# method calling to merge the elements
list1.head=MergingTwoSortedList(list1.head,list2.head)
list1.print()

        








