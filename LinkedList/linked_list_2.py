# ??????????

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, d):
        temp_node = Node(d)
        n = self
        while n.next != None:
            n = n.next
        n.next = temp_node

    def is_palindrom(self):
        temp = []
        n = self
        if not n or n.next is None:
            return True
        while n != None:
            temp.append(n.data)
            n = n.next
        #print('temp = ', temp)
        #print(temp[::-1])
        return temp == temp[::-1]

    def insert_node(self, place_after_element_number, newdata):
        temp_node = Node(newdata)
        n = self
        count = 1
        while n.next != None and count < place_after_element_number:
            count += 1
            n = n.next
        temp_node.next = n.next
        n.next = temp_node

    def __str__(self):
        rez = ''
        n = self
        while n.next != None:
            rez += str(n.data)
            rez += ' -> ' if n.next else ''
            n = n.next
        rez += str(n.data)
        return rez

    def reverse_linked_list(self, tail=None):  # not
        tail = head = self
        print()
        print('---', tail.data)
        while tail.next != None:
            tail = tail.next
            print('---', tail.data)
        while head:
            head.next, tail, head = tail, head, head.next

        return tail
        
          

class NewNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse_new_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

def print_list(head, end='\n'):
    n = head
    while n:
        print(n.data, end=' -> ' if n.next else '')
        n = n.next
    print(end)



        
        
        
if __name__ == '__main__':
    # 1
    N = Node(1)
    N.append_to_tail(2)
    N.append_to_tail(3)
    N.append_to_tail(4)
    print_list(N)
    print('palindrom = ', N.is_palindrom())

    # 2
    N = Node(1)
    N.append_to_tail(2)
    N.append_to_tail(2)
    N.append_to_tail(1)
    print_list(N)
    print('palindrom = ', N.is_palindrom())
    
    # 3   
    print(N)
    N.insert_node(2, 100)
    print(N)
    print('palindrom = ', N.is_palindrom())

    print('---' * 10)
    # 4
    M = NewNode(1, NewNode(2, NewNode(3, NewNode(4))))
    print_list(M)
    print('reverse')
    print_list(reverse_new_list(M))
          
        
