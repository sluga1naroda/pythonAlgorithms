# Напишите программу, которая будет читать выражение в обратной польской записи и выводить его значение. 
# В обратной польской записи операция записывается после двух операндов. Например, сумма двух чисел 2 и 3 записывается как 2 3 +. 
# Запись 2 3 + 4 * обозначает привычное нам (2 + 3) * 4, а запись 6 7 8 + 3 * + означает 6 + (7 + 8) * 3. Достоинство такой записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.
# Числа и операторы в выражении разделены пробелом. Используются только операторы +,  - и *
def reversepolishnotation(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '/':
                result = operand1/operand2
            elif token == '*':
                result = operand1*operand2
            stack.append(result)
    return stack

expression = input()
result = reversepolishnotation(expression)
print(result[0])