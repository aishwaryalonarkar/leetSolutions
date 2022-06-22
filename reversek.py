# Reverse Nodes in k-Group
# Question Source : https://leetcode.com/problems/reverse-nodes-in-k-group/

class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self) :
        self.head = None
    
    def addList(self, llist) :
        data_temp = None 
        for i in llist :
            data_n = Node(i) 
            if self.head == None :
                self.head = data_n
            data_n.next = None
            if data_temp != None :
                data_temp.next = data_n
            data_temp = data_n
        # self.printList()

    def printList(self) :
        data_temp = self.head 
        while(data_temp) :
            print(data_temp.data)
            data_temp = data_temp.next

    def reverseList(self, k) :
        current = self.head
        prev = None
        kth = None
        while(current) :
            next = current.next
            if current.data != k :
                current.next = prev
                prev = current
            else : 
                kth = current
                kth.next = None
            current = next
        kth.next = prev
        self.head = kth
        self.printList()


l = LinkedList()
l.addList([11,2,3,4,5])
l.reverseList(3)