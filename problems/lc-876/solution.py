from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution: 
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

def convert_linked_list_to_list(start_node: ListNode):
    current = start_node
    result = []
    while current != None:
        result.append(current.val)
        current = current.next
    return result

def main(): 
    test1 = ListNode(1, ListNode(2, (ListNode(3, ListNode(4, ListNode(5, None))))))
    test2 = ListNode(1, ListNode(2, (ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))))

    solution = Solution()

    result1 = solution.middleNode(test1)
    result2 = solution.middleNode(test2)

    print(convert_linked_list_to_list(result1))
    print(convert_linked_list_to_list(result2))

if __name__ == '__main__':
    main()
