#Задано символьний рядок. Розробити програму, яка вилучає з цього рядка
#всі повторні входження цифр і знаків арифметичних операцій.

n = "1 + 3 * 4 - 6 * 5 = 7 / 1 + 4 - 6"
print(n)
st = ""
#create list of numbers and arithmetic symbols
num_sym = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/')
for char in (n):
    if char not in st or char not in num_sym:
        st += char
print(st)
