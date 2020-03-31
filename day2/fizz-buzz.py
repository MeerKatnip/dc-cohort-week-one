number = int(input('Input a whole number: '))

if (number % 3) == 0 and (number % 5) == 0: # this needs to check if it is divisible by BOTH 3 and 5
    print('Fizz Buzz')
elif (number % 3) == 0: # will run only if the above is not True
    print('Fizz') 
elif (number % 5) == 0: # will run only if both the above are not True
    print('Buzz')       
else: # will run only if none all three conditions above are False
    print('This number IS NOT divisible by 3 or 5')