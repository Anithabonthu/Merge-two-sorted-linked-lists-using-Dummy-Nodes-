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
    def swapNodes(self,head,k):
        last=first=head
        for i in range(1,k):
            first=first.next
        checker=first
        while checker.next:
            last=last.next
            checker=checker.next
        temp=last.data
        last.data=first.data
        first.data=temp
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
#To swap the nodes read the k value
k=int(input("Enter k value: "))
list1.swapNodes(list1.head,k)
print("After Swapping the nodes")
list1.print()

    


# ## 

# In[ ]:




