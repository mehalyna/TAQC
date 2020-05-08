GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}

name = str(input("Input name: "))

def greeting(name):
    if name in GUEST_LIST:
        return ("Hi! I'm %s, and I'm from %s" %(name, GUEST_LIST[name]))
    else:
        return ("Hi! I'm a guest")

print(greeting(name))
