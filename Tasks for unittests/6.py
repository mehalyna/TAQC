#Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

def format_date(date):
    new_date = date.split('/')
    return (str(new_date[2]+new_date[1]+new_date[0]))

print(format_date("08/17/2020"))
