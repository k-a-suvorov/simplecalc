#Simple calc

operations_math = ['+', '-', '*', '/']
print('This is simle calc')
try:
	a = float(input('a = '))
	b = float(input('b = '))

	choice = input('Please input math operations:  +, -, *, / and get result for you') 

	if choice == operations_math[0]:
		print(a+b)
	elif choice == operations_math[1]:
		print(a-b)
		print(b-a)
	elif choice == operations_math[2]:
		print(a*b)
	elif choice == operations_math[3]:
		print(a/b)
		print(b/a)
	else:
		print('Incorrect input')
except ValueError:
    print('Next time, please insert correct integer numbers!')
except ZeroDivisionError:
    print('On zero share cannot be!')
