# Is this number divisible by 3

number_to_check = int(input('Input a whole number: '))

# True / False
# 0 < 100 True
# 0 == 1 False

if (number_to_check % 3) == 0: # if True, this line will run
    print('This number IS divisible by 3')
elif (number_to_check % 5) == 0: # will run only if the above is not True
    print('This number IS divisible by 5')    
else: # will run if both lines above are not True
    print('This number IS NOT divisible by 3 or 5')