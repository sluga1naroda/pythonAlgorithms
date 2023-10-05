# Вам дан отсортированный по убыванию список. Вставьте новое число так, чтобы список продолжался оставаться отсортированным по убыванию. 
# Sample Input:
# 20->15->15->14->13->13->13->11->9->7->7->6->6->4->4->4->3->3->1->1 6
# Sample Output:
# 20->15->15->14->13->13->13->11->9->7->7->6->6->6->4->4->4->3->3->1->1

class Solution:
    def insertIntoSorted(self, head: ListNode, new_value: int) -> ListNode:
        s = p = head
        while s.next and s.val > new_value:
            p,s = s, s.next
        a = ListNode(new_value)
        a.next = s
        if p == head:
            head = a
        else:
            p.next = a
        return head