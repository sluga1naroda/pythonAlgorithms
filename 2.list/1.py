# Вам дан односвязный список. Значение, лежащее в каждой Node списка: 0 или 1. Ваша задача вернуть десятичное представление числа по его бинарному представлению, хранящемуся в списке. 
# Sample Input:
# 1->1->0->1->0->1->0->1->0->1->1->1->0->0->1->0->1->0->0->1->0->1->1->0
# Sample Output:
# 13988502

class Solution:
    def getDecimalValue(self, head: ListNode) -> int: 
        result = 0
        current = head
    
        while current:
            result = result * 2 + current.val  # Умножение на 2 и добавление значения текущей ноды к результату
            current = current.next  # Переход к следующей ноде
        
        return result