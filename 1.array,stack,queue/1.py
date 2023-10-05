# Для начала простая задача, чтобы познакомить вас с ограничениями на память и время.
# Напишите функцию, которая принимает имя файла, читает из него целые числа и возвращает их сумму.
# Каждое число на новой строке.\
# Если файл пустой, то функция должна возвращать 0.

def sum_numbers(filename):
    file = open(filename, "r")
    
    sum = 0
    while True:
        line = file.readline()
        if not line:
            break
        sum += int(line)
    
    file.close
    
    return sum