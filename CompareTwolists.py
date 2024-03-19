#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data !=llist2.data:
            return 0
        llist1=llist1.next
        llist2=llist2.next
    if not llist1 and not llist2:
        return 1
    else:
        return 0
list1=LinkedList()
print("Enter Elements into List1.")
flag=True
while flag:
    value=int(input("Enter data value: "))
    list1.insert(value)
    ch=input("Do you want insert yes/no").lower()
    if ch=='yes':
        flag=True
    else:
        flag=False        
list2=LinkedList()
print("Enter Elements into List2.")
flag=True
while flag:
    value=int(input("Enter data value: "))
    list2.insert(value)
    ch=input("Do you want insert yes/no").lower()
    if ch=='yes':
        flag=True
    else:
        flag=False   
print(compare_lists(list1.head,list2.head))


# In[ ]:





# In[ ]:




