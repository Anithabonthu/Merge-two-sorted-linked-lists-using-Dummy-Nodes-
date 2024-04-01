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
                print(temp.data)
                temp=temp.next
def merge(list1,list2):
        while list2:
            new=list1.next
            list1.next=list2
            list1=list2
            list2=new
def reverse(head):
        if not head:
            return None
        prev=None
        curr=head
        ptr=curr.next
        while curr.next:
            curr.next=prev
            prev=curr
            curr=ptr
            ptr=ptr.next
        curr.next=prev
        return curr
def reorderList(head):
        if not head or not head.next:
            return
        slow=head
        fast=head
        prev=head
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        prev.next=None
        list1=head
        list2=reverse(slow)
        merge(list1,list2)
l=LinkedList()
while True:
    print("1.Insertion  2.exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        val=int(input("Enter the data:"))
        l.insert(val)
    elif ch==2:
        break
reorderList(l.head)
l.print()
        


# In[ ]:





# In[ ]:




