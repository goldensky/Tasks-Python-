# https://leetcode.com/problems/merge-two-sorted-lists/description/


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def append_to_tail(self, d):
        temp_node = Node(d)
        n = self
        while n.next != None:
            n = n.next
        n.next = temp_node
       

    def __str__(self, end='\n'):
        rez = ''
        head = self
        while head.next != None:
            rez += str(head.val) + ' -> '
            head = head.next
        rez += str(head.val)
        return rez

    def delete_node(self, place_after_num): # after node number
        head = self
        count = 1
        while head.next.next != None and count < place_after_num:
              head = head.next
              count += 1
        head.next = head.next.next

    def delete_middle_node(self): 
        fast = slow = self
        while fast.next!= None:
            fast = fast.next
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp_list = Node(0)
        p = temp_list
        
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
                
        if l1:
            p.next = l1           
        elif l2:
            p.next = l2
        return temp_list.next



if __name__ == '__main__':      
    print('LIST 1')
    list1 = Node(1)
    list1.append_to_tail(2)
    list1.append_to_tail(4)
    print(list1)
    print()
    
    print('LIST 2')
    list2 = Node(1)
    for item in [3, 5, 6, 7]:
        list2.append_to_tail(item)
    print(list2)

    s = Solution()
    merge_list = s.mergeTwoLists(list1, list2)
    print(merge_list)

    merge_list.delete_node(3)
    print(merge_list)

    merge_list.delete_middle_node()
    print(merge_list)
    '''
    LIST 1
    1 -> 2 -> 4

    LIST 2
    1 -> 3 -> 5 -> 6 -> 7
    1 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
    1 -> 1 -> 2 -> 4 -> 5 -> 6 -> 7
    1 -> 1 -> 2 -> 4 -> 6 -> 7                         
    '''
    

    
    





