

class Solution:
    def reorderList(self, head: ListNode, tail: ListNode) -> ListNode:
        if not head or not tail:
            return head

# Находим середину списка
        slow, fast = head, head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next

        # Разделяем список на две половины
        left_head, left_tail = head, slow
        right_head, right_tail = slow.next, tail

        # Обрываем связь между половинами
        left_tail.next = None
        right_head.prev = None

        # Разворачиваем вторую половину
        prev = None
        current = right_head
        while current:
            next_node = current.next
            current.next = prev
            current.prev = None
            prev = current
            current = next_node
        right_head = prev

        # Объединяем обе половины
        current_left, current_right = left_head, right_head
        while current_right:
            next_left = current_left.next
            next_right = current_right.next
            current_left.next = current_right
            current_right.prev = current_left
            current_right.next = next_left
            if next_left:
                next_left.prev = current_right
            current_left = next_left
            current_right = next_right

        return left_head