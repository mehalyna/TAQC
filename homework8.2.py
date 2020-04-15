#Створіть словник, ключами є слова, а значеннями – список слів-синонімів до
#нього. Програма отримує на вхід кількість слів N. Далі користувач вводить
#слова-ключі та відповідні йому синоніми. 
#Передбачити: 
#1) на запит (слово) користувача вивести список синонімів;
#2) користувач вводить речення, в якому є слова (ключі, що містяться в словнику).
#Замінити їх синонімами та вивести речення на екран.

synonyms = {
    'beautiful':['cute', 'good-looking', 'lovely', 'handsome', 'pretty'],
    'great':['big', 'strong', 'perfect', 'good', 'fine'],
    'happiness':['pleasure', 'joy','satisfaction', 'euphoria']}
print("Hello. This is dictionary of synonyms.")
print("Synonyms:", synonyms)
print("Let's add several new words and synonyms.\nIf you want to stop enter word 'End'")
#first part
while 1==1:
    key_word = input("Input key-word: ")
    if key_word == 'End':
        break
    key_w = ""
#verify if key_word is in synonyms already
    for key in synonyms:
        if key_word in synonyms[key]:
            key_w = key
    if key_w !="":
        print("Word %s is synonym for %s" %(key_word,key_w))
        continue
    if key_word in synonyms:
        print("Key_word %s is already in dict" %(key_word))
        continue
#add synonyms
    values = []
    while 1==1:
        synonym = input("Input synonym: ")    
        if synonym == 'End':
            break
        elif synonym not in values:
            values.append(synonym)
    synonyms.update({key_word : values})
print("Synonyms: ", synonyms)

#second part
row = input("Input some sentence: ")
r = row.split()
for i in r:
    if i in synonyms:
        row = row.replace("%s" %(i), "%s" %(synonyms[i][0]))
print("Your sentence with replaced by a synonym: ", row)


