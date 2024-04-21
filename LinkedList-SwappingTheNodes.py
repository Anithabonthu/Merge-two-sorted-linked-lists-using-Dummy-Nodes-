#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
    def traverse(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
    def SwapNodes(self,head):
        if not head or not head.next:
            return head
        dummy=Node(0)
        dummy.next=head
        prev=dummy
        while head and head.next:
            slow,fast=head,head.next

            prev.next=fast
            slow.next=fast.next
            fast.next=slow
            
            prev=slow
            head=slow.next
        return dummy.next

l=LinkedList()
while True:
    print("1.Insert   2.Traverse  3.Swap nodes 4.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        l.insert(value)
    elif ch==2:
        l.traverse()
    elif ch==3:
        l.head=l.SwapNodes(l.head)
        print("After Swapping the Node:")
    elif ch==4:
        break


# In[ ]:




