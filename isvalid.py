import unittest

def isvalid(s):
    stack = []
    left = '([{'
    right = ')]}'
    if s == '':
        return True
    for index, char in enumerate(s):
        if char in left:
            stack.append(char)
        elif char in right:
            if stack:
                if left.index(stack[-1]) != right.index(char):
                    return False
                stack.pop()
            else:
                return False
    return len(stack) == 0

    
class TestSolution(unittest.TestCase):
    def test_wrong_answer_many(self):
        self.cases = ['(', ']', '{]', '((])', '(()()))', '([)]', '{)}]', ']', 
                        '}', ')', '(()'
                      ]
        for s in self.cases:
            with self.subTest(case=s):
                result = isvalid(s)
                self.assertFalse(result)

    def test_right_answer_many(self):
        self.cases = ['()', '[]', '{}', '(()(){[]{}()()((()))})', 
                      '(()[{}{}()]())', '{}', '[{()}]', '{}[]()', '{{{()[]}}}',
                        ]
        for s in self.cases:
            with self.subTest(case=s):
                result = isvalid(s)
                self.assertTrue(result)
        
    def test_wrong_answer(self):
        s = '(()()))'
        result = isvalid(s)
        self.assertFalse(result)

    def test_right_answer(self):       
        s = '(){}[]'
        result = isvalid(s)
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()






        
