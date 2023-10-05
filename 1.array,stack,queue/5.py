# Вам дана строка 0 и 1. 0 означает, что в магазин пришел новый посетитель. 1 означает, что посетителя обсужили. 
# Сколько изначально должно было быть человек в очереди (минимальное количество), чтобы сценарий был реализуем (нельзя обслужить посетителя, если очередь пуста).,
# Sample Input:
# 0 1 0 1 1 0 1
# Sample Output:
# 1

def minimuminitialqueuelength(sequence):
    count = 0
    balance = 0

    for char in sequence.split(' '):
        if char == '0':
            balance += 1
        elif balance == 0:
            count += 1
        else:
            balance -= 1

    return count


sequence = input()
result = minimuminitialqueuelength(sequence)
print(result)