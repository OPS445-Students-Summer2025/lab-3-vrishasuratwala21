#!/usr/bin/env python3

#return_text_value() function
#Author ID: vvsuratwala 

def return_text_value():
	return "Hello, welcome to OPS445 Lab 3! This is Vrisha"

#return_number_value() function

def return_number_value():
	a = 10
	b = 20
	return a + b 

#Main program 
if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))
