# Вам дан односвязный список. Разверните список.
# Sample Input:
# 19->20->8->20->16->8->16->1->2->2->8->15->17->13->18->7->5->10->4->16
# Sample Output:
# 16->4->10->5->7->18->13->17->15->8->2->2->1->16->8->16->20->8->20->19

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev