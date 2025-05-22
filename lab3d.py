#!/usr/bin/env python3
'''Lab 3 Part 2 - free space check'''
#Author id: vvsuratwala 

import subprocess 

def free_space():
	result = subprocess.run("df -h | grep '/$' | awk '{print $4}' ",
				shell=True,
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,
				text=True)
	return result.stdout.strip()

if __name__ == '__main__':
	print(free_space())
