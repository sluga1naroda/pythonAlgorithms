# На детской площадке поставили новую горку и все дети хотят на ней покататься. В результате образовалась очередь. 
# Но дети бывают разные: скромные и наглые. Скромные дети встают в конец очереди. Наглые дети встают ровно в середину, а если в очереди нечетное число детей, то сразу за тем, кто стоит в середине очереди. 
# На вход подается несколько строк. В первой строке - количество строк, которое вам нужно будет прочитать. Во всех остальных может быть:
# пара вида `s N` или `i N`, где символ s означает скромного ребенка, символ i – наглого, а N – номер ребенка.
# символ `+`, который означает, что ребенок, который стоял первым в очереди, скатился с горки.
# Напишите программу, котора выведет номера скатившихся детей.
# Sample Input 1:

# 5
# s 1
# s 2
# i 3
# +
# +
# Sample Output 1:

# 1
# 3
# Sample Input 2:

# 5
# s 1
# s 2
# +
# i 3
# +
# Sample Output 2:

# 1
# 2

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

    def __str__(self):
        return self.val

kid_count = 1
n = int(input())
first_kid = ListNode(input().split(sep=' ')[1])
tail_kid = first_kid
mid_kid = first_kid
head_kid = first_kid
for i in range(n-1):
#print(f'loop {i+1}')
    a = input()
    if a == '+':
        print(int(head_kid.val))
        head_kid = head_kid.next
        if kid_count%2 == 0:
            mid_kid = mid_kid.next
        kid_count-=1
    else:
        b = a.split(sep=' ')
        char = b[0]
        num = b[1]
        kid = ListNode(num)
        if char == 's':
            kid.prev = tail_kid
            kid.prev.next = kid
            tail_kid = kid
            if (kid_count+1)%2 == 1:
                mid_kid = mid_kid.next
        else:
            kid.prev = mid_kid
            kid.next = mid_kid.next
            try:
                mid_kid.next.prev = kid
            except:
                pass
            mid_kid.next = kid
            if kid_count%2 == 0:
                mid_kid = mid_kid.next
            if kid.next is None:
                tail_kid = kid

        kid_count+=1