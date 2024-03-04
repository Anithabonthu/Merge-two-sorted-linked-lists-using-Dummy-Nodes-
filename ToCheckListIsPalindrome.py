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
def ToCheckPalindrome(list):
    stack=[]
    ptr=list
    while ptr:
        stack.append(ptr.data)
        ptr=ptr.next
    ispalin=True
    while list:
        i=stack.pop()
        if i==list.data:
            ispalin=True
        else:
            ispalin=False
        list=list.next
    return ispalin
l=LinkedList()
while True:
    print("1.Insertion  2.Traverse  3.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        l.insert(value)
    elif ch==2:
        l.print()
    elif ch==3:
        break
l=ToCheckPalindrome(l.head)
if l==True:
    print("Linked List is Palindrome")
else:
    print("Linked List is not  Palindrome")

