#usr/bin/python3
#Simple calc

print('This is simle calc')
try:

	check = True

	while check:
		if (not input):
			print('Next time try to use the calculator again or you want to exit now!')
			check = False
		else:

			print('This is the simple calculator. Press \"Enter\" to exit')
			#block of userinput
			a = float(input('a = '))
			b = float(input('b = '))


			#block of proccessing
			switch = {
				'+' : lambda a, b: a + b,
				'-' : lambda a, b: a - b,
				'*' : lambda a, b: a * b,
				'/' : lambda a, b: a / b,
				'**' : lambda a, b: a ** b

			}


			#Blocks of outputs
			result = switch['+'](a, b)
			print(F"a + b = {result}")
			result = switch['-'](a, b)
			print(F"a - b = {result}")
			result = switch['*'](a, b)
			print(F"a * b = {result}")
			result = switch['/'](a, b)
			print(F"a / b = {result}")
			result = switch['+'](a, b)
			print(F"a ** b = {result}")



except ZeroDivisionError:
    print('On zero share cannot be!')		
except ValueError:
    print("You have some mistake of userinput Value")
except TypeError:
   print("You have some mistake of type Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )
