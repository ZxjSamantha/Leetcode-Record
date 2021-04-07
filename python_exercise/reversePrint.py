# Definition for singly-linked list.
import numpy as np

class ListNode:
    def __init__(self, x):
          self.val = x
          self.next = None 
# Stack 

class Solution1:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next 
        return stack[::-1]

# Recurrent 
class Solution2:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head.next = None:
            return []
        if head:
            return self.reversePrint(head.next) + [head.val]

if __name__=='__main__':
    case = Solution2()
    testList = [np.random.randint(1,30) for i in range(30)]
    test = case.reversePrint(testList)
    print(test)

        
        



