
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = Node(None) #Head node - unindexable
    
    def append(self, data):
        add = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = add

    def length(self):
        leng = 0
        cur = self.head
        while cur.next != None:
            leng += 1
            cur = cur.next
        return leng
    
    #swap given node and right node
    def rswap(self, left_index):
        count = -1
        prev = None
        cur = self.head
        if left_index + 1 <= self.length():
            while count != left_index:
                prev = cur
                cur = cur.next
                count += 1
            prev_next = prev.next
            cur_next = cur.next
            cur_next_next = cur.next.next
            prev.next = cur_next
            cur.next.next = prev_next
            cur.next = cur_next_next
        
    def get(self, index):
        cur = self.head
        count = -1
        while count != index:
            cur = cur.next
            count += 1
        return cur.value

    def display(self):
        dis = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            dis.append(cur.value)
        return dis

  
def BubbleSort(linked_list: LinkedList()):
    x = linked_list.length()
    for i in range(x):
        for j in range(0, x-i-1):
            if linked_list.get(i) > linked_list.get(i + 1):
                linked_list.rswap(i)
    print(linked_list.display())


    

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(9)
ll.append(0)
ll.append(5)

BubbleSort(ll)