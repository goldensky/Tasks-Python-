
# https://leetcode.com/problems/palindrome-number/description/

def palindrome(s):
    news = str(s)
    print(news, news[::-1])
    return news == news[::-1]


# https://leetcode.com/problems/palindrome-linked-list/description/
class Node:
    def __init__(self, x, next = None):
        self.x = x
        self.next = next

class Solution:
    def isPalindrome(self, head):
        if not head or head.next is None:
            return True
        temp = []
        is_palindrome = False

        while head != None:
            temp.append(head.x)
            head = head.next
            
        if temp == temp[::-1]:
            is_palindrome = True
        return is_palindrome


if __name__ == '__main__':
    print('PALINDROME')
    s = -121
    print(palindrome(s))
    print()
    
    print('NODE')
    head = Node(1, Node(2, Node(2, Node(1))))
    s = Solution()
    print(s.isPalindrome(head))






    
