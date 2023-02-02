# Assignment 1 Looking for Fermat's Last Theorem Near Misses 
# File Name: assignment_1_Group1.py
# Jose Montes De Oca Morfin, Paige Dyer, Jacob Toth
# jacobtoth@lewisu.edu
# PaigeDyer@lewisu.edu
# joseamontesdeocamo@lewisu.edu
# CPSC-44000-LT1
# Finished and Submitted: 02/02/2023 
# This program adds two numbers to the same power, (x**n + y**n), and tries to find a the closest possible z**n to make this expression true (x**n + y**n = z**n)


import math

print("")
print("Hello, welcome to the Looking for Fermat's Last Therorem Near Misses program. ")
print("In this program you will be asked to select a 'n' power and a maximum number.")
print("What this program does, is it goes through every combination of numbers from 1 - the max")
print("and it will raise them both to the 'n'th power that was selected and add the two.")
print("Then it will try and find the closest possible number 'z' that makes this equation true...")
print("(x^n) + (y^n) = (z^n)")
print("")

success = False 
while success == False:             # this loops keeps looping until the user inputs a number greater than 2 and less than 12 
    power = int(input("Enter the power you want to use: "))  # power that we will raise x, y, and z too  (must be between 2 and 12)
    if power <= 2 or power >= 12:
        success = False
        print("Please enter a number greater than 2 and less than 12")
    else:
        success = True

success = False
while success == False:             # this loop will keep looping until the user enters a number greater than or equal to 10 for k 
    max = int(input("Enter the max number you want to compare (minimum must be 10): "))      # this is k (there is no max)
    if max < 10:
        success = False
        print("You must select a number greater than or eqaul to 10")
    else:
        success = True


smallest_miss_percentage = 100      # this is set as the initial miss percentage just to use it to compare every other miss percentage. If there is a miss smaller than this, then it becomes the smallest miss

for i in range(10, max + 1):                            # Here we are going to do two loops, one to cycle every first number combination, and the next to cycle the next number combination from 1-k
    for j in range(10, max + 1):                        # this is the second number combinaiton
        x_y_sum = i ** (power) + j ** (power)         # This gets the exact number of (x**n + y**n)
        z_exact = (x_y_sum ** (1/power))              # this gets the exact number of z by taking the nth root of z 
        z = math.floor(z_exact)                       # this generates the natrual number of z by rounding z down
        z_1 = z + 1                                   # this gets z + 1
        z_n = z ** power                              # this gets z**n
        z_1_n = z_1 ** power                          # this gets (z + 1) ** n
        
        difference1 = (x_y_sum) - (z_n)               # this finds the difference between ((x**n + y**n) - z**n)
        difference2 = (z_1_n) - (x_y_sum)             # this finds the difference between ((z+1)**n - (x**n + y**n))
        
        if difference1 < difference2:                 # this conditional finds the smallest of the two misses 
            miss = difference1
        else:
            miss = difference2
            
        relative_size_miss = miss / x_y_sum            # this gets the decimal of the miss 
        relative_percentage = relative_size_miss * 100  # this turns that decimal to a percentage 
        
        if relative_percentage < smallest_miss_percentage :     # this uses that earlier smallest_miss_percentage variable to compare with the current miss and see which is smaller. 
            smallest_miss_percentage = relative_percentage      # if the current miss is smaller, then it records it as the now current smallest miss and will use this one to compare to the next one, instead of the default one
            smallest_x = i                                      # these next variables simply record the current x, y, z and miss for the current cycle that is the smallest miss
            smallest_y = j
            smallest_z = z
            smallest_miss = miss
            print("X : %d\nY: %d\nZ: %d\nActual Miss: %d\nRelative Miss: %.4f%%" % (i, j, z, miss, relative_percentage))
            print("")
        
        
        
print("The smallest possible miss was...\nX: %d\nY: %d\nZ: %d\nActual Miss: %d\nSmallest Relative Miss: %.4f%%" % (smallest_x, smallest_y, smallest_z, smallest_miss, smallest_miss_percentage))
print("")
    



