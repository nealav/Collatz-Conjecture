# Collatz function; calls the function repeatedly until it returns 1


global_input = int(raw_input('Enter a number: '))

def Collatz():
	global global_input
	if global_input%2 == 0:
		print global_input//2
		global_input = global_input//2
	elif global_input == 0:
		print "You have not entered a legal number"
	else:
		print global_input*3 + 1
		global_input = global_input*3 + 1
		
while global_input != 1:
	Collatz()
