# Вам дан двусвязный список. Определите является ли число, представленное списком - палиндромом. 
# Sample Input:
# 2<->1<->8<->18<->6<->1<->13<->8<->11<->10<->12<->8<->19<->14<->13<->15<->4<->3<->15<->15
# Sample Output:
# False

class Solution:
    def isPalindrome(self, head: ListNode, tail: ListNode) -> bool:
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        return values == values[::-1]