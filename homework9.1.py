#Написати функцію arithmetic, яка приймає 3 аргументи: перші 2 - числа,
#третій - операцію, яка повинна бути здійснена над ними. Якщо третій
#аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити
#(перше на друге). В інших випадках повернути рядок "Невідома операція".

a = int(input("Input a: "))
b = int(input("Input b: "))
oper = input("Input operation(+,-,*,/): ")

def arithmetic(a,b,oper):
    if oper == '+':
        return (a+b)
    elif oper == '-':
        return (a-b)
    elif oper == '*':
        return (a*b)
    elif oper == '/':
        if b == 0:
            return ("Error, b shouldn't = %d" %(b))
        else:
            return (a/b)
    else:
        return ("Unknown operation")
    
print("Result: ", arithmetic(a,b,oper))
