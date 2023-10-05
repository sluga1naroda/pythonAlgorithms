# Вам дан односвязный отсортированный список. Избавьтесь от дупликатов так, чтобы в списке содержались только уникальные элементы.
# Sample Input:
# 1->4->6->7->9->9->10->11->14->14
# Sample Output:
# 1->4->6->7->9->10->11->14

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head