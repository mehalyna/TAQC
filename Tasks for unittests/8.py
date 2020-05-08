#The volume of a spherical shell is the difference between the enclosed
#volume of the outer sphere and the enclosed volume of the inner sphere:
#Create a function that takes r1 and r2 as arguments and returns the volume
#of a spherical shell rounded to the nearest thousandth.

from math import pi

def vol_shell(r1, r2):
    volume = 4/3*pi*r1**3 - 4/3*pi*r2**3
    return(round(volume, 3))

print(vol_shell(5, 3))
    
