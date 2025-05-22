#!/usr/bin/env python3

#return_text_value() function
#Author ID: vvsuratwala

def return_text_value():
	name = "Terry"
	greeting = "Good Morning " + name 
	return greeting 

#return_number_value() function 

def return_number_value():
	n1 = 10
	n2 = 5
	n3 = n1 + n2
	return n3

#Main program

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))
