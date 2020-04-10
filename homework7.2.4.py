#Задано символьний рядок,. Розробити програму, яка знаходить групи цифр,
#записаних підряд, і вилучає із них всі початкові нулі, крім останнього,
#якщо за ним знаходиться крапка. Друкує модифікований масив по сорок
#символів у рядку

r = "ksdjvh.kvjh000.000s64jhsfvsjh00000.tfgsdkfv00.5hbsd0.k"
print("r:", r)
print("Lengh r: %d" %(len(r)))
i = '0'
while "00." in r:
    r = r.replace("00.", "0.")
print("r:", r)
print("Lengh r: %d" %(len(r)))
#print only 0 characters in row
print("First 40 characters:",r[0:40],"\nSecond 40 char:",r[40:80])
