a = []
letters = []
numbers = []
symbols = []
for i in range (33,127):
    a.append(chr(i))
    if i<=47:
       symbols.append(chr(i))
    elif i<=57:
        numbers.append(chr(i))
    elif i<=64:
        symbols.append(chr(i))
    elif i<=90:
        letters.append(chr(i))
    elif i<=96:
        symbols.append(chr(i))
    elif i<=122:
        letters.append(chr(i))
    elif i<=127:
        symbols.append(chr(i))
        
# turn list in tuple
print("Letters: ", tuple(letters))
print("Numbers: ", tuple(numbers))
print("Symbols: ", tuple(symbols))

# print index
x = input("Enter only ONE letter/number/symbol: ")
if x in letters:
    print("Index of entered letter is: ", letters.index(x))
if x in numbers:
    print("Index of entered number is: ", numbers.index(x))
if x in symbols:
    print("Index of entered symbol is: ", symbols.index(x))

# reverse of tuple numbers
num = tuple(reversed(numbers))
print("Reversed tutle of numbers: ", num)
