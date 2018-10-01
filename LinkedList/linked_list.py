

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_list(head, end='\n'):
    while head:
        print(head.data, end = ' -> ' if head.next else '')
        head = head.next
    print(end=end)


def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail



if __name__ == '__main__':
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print_list(head)
    print_list(reverse_list(head))
