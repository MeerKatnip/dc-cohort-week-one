print('Tip Calculator')
total_amount = input('How much was the bill in total?')

tip_percentage_amount = input('How much do you want to tip? (1-100%)')

decimal = float(tip_percentage_amount) / 100

print('Your tip will be: ')
print(float(total_amount) * float(decimal))

# 1+
#print(100*0.1)