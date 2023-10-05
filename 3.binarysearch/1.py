# В этой задаче вам дан отсортированный по возрастанию список чисел и некоторое заданное число. Верните индекс заданного числа в списке или -1, если данное число отсутствует в нем.

# Sample Input:

# [2,3] 2
# Sample Output:

# 0
class Solution:
    def search(self, list_num, to_search: int):
        first_index = 0
        size = len(list_num)
        last_index = size - 1
        mid_index = (first_index + last_index) // 2
        mid_element = list_num[mid_index]
        is_found = True
        while is_found:
            if first_index == last_index:
                if mid_element != to_search:
                    is_found = False
                    return -1
            elif mid_element == to_search:
                return mid_index
            elif mid_element > to_search:
                new_position = mid_index - 1
                last_index = new_position
                mid_index = (first_index + last_index) // 2
                mid_element = list_num[mid_index]
                if mid_element == to_search:
                    return mid_index
            elif mid_element < to_search:
                new_position = mid_index + 1
                first_index = new_position
                last_index = size - 1
                mid_index = (first_index + last_index) // 2
                mid_element = list_num[mid_index]
                if mid_element == to_search:
                    return mid_index
        return -1