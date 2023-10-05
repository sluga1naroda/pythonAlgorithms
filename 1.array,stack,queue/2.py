# Напишите программу, которая будет принимать строку символов и проверять правильно или нет в ней расставлены скобки.
# Скобок три вида: круглые (), квадратные [] и фигурные {}.
# В строке, в которой нет скобок, нет и ошибок. Если взять строку без ошибок и обернуть открывающей скобкой слева, а закрывающей скобкой того же вида справа, то будет строка без ошибок. Если взять две строки без ошибок и записать их одну за другой, то получится строка без ошибок.
# Если в прочитанной строке ошибок в расстановке скобок нет, то выведите "CORRECT" (без кавычек), иначе "WRONG" (без кавычек).

s = input()

goodFlag = True
savingArray = []

for i in s:
    if i in '{([':
        savingArray.append(i)
    elif i in '})]':
        if not savingArray:
            goodFlag = False
            break
        elem = savingArray.pop()
        if elem == '{' and i == '}':
            continue
        if elem == '(' and i == ')':
            continue
        if elem == '[' and i == ']':
            continue
        goodFlag =False
        break
if goodFlag and len(savingArray) == 0:
    print('CORRECT')
else:
    print('WRONG')