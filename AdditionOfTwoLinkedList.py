#!/usr/bin/env python
# coding: utf-8

# In[6]:


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
                print(temp.data,end=" ")
                temp=temp.next
    def Reverse(self):
        prev=None
        curr=self.head
        ptr=curr.next
        while curr.next != None:
            curr.next=prev
            prev=curr
            curr=ptr
            ptr=ptr.next
        curr.next=prev
        self.head=curr
        list1.print()
        
def add(list1,list2): 
    dummy=temp=Node(0)
    total=carry=0
    while list1 or list2 or carry:
        total=carry
        if list1:
            total+=list1.data
            list1=list1.next
            
        if list2:
            total+=list2.data
            list2=list2.next
        num = total %10
        carry = total //10
        temp.next=Node(num)
        temp=temp.next
        
    return dummy.next
                
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
list1.head=add(list1.head,list2.head)
list1.Reverse()      #Reversing the list 


# In[ ]:





# In[ ]:





# In[ ]:




