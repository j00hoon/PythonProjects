from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        len = 0

        while tmp is not None:
            len += 1
            tmp = tmp.next

        if len < n:
            return head
        else:
            target = len - n
            i = -1

            if target == 0:
                head = head.next
            else:
                tmpHead = head
                prev = tmpHead

                while tmpHead is not None:
                    if i + 1 != target:
                        prev = tmpHead
                    else:
                        if tmpHead.next is not None:
                            prev.next = tmpHead.next
                            break
                        else:
                            prev.next = None
                    tmpHead = tmpHead.next
                    i += 1
        return head





solution = Solution()
# list = [1, 2, 3, 4, 5]
list = [1]
# list = [1, 2]
head = ListNode(list[0])
tail = head

i = 1
while i < len(list):
    tail.next = ListNode(list[i])
    tail = tail.next
    i += 1

head = solution.removeNthFromEnd(head, 1)

tmp = head
while tmp != None:
    print(tmp.val)
    tmp = tmp.next