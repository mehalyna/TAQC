#Користувач робить внесок в розмірі n гривень строком на years років під 10%
#річних (щороку розмір його внеску збільшується на 10%. Ці гроші додаються
#до суми вкладу, і на них в наступному році теж будуть відсотки).
#Написати функцію bank, яка приймає аргументи n і years, і повертає суму,
#яка буде на рахунку користувача.

n = int(input("Input amount of grn: "))
years = float(input("Input years: "))

def bank(n, years):
    if years == 0:
        return (n)
    else:
       # n += n*0.1(bank(years-1)
        return(bank((n + n*0.1), (years - 1)))

print("Sum: ", bank(n,years))

