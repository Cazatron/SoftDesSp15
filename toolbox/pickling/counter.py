""" A program that stores and updates a counter using a Python pickle file"""

import os
from os.path import exists
import sys
#from pickle import dump, load
import pickle

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will be incremented.

		file_name: the file that stores the counter to be incremented.  If the file doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be reset.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
	if not os.path.exists(file_name):
		file1 = open(file_name, 'w')
		file1.write(pickle.dumps(1))
	else:
		file1 = open(file_name, 'r+')
		contents = file1.read()
		file1.seek(0,0)

		if reset or contents == '':
			file1.write(pickle.dumps(1))
		else:
			integer_contents = pickle.loads(contents)
			integer_contents += 1
			file1.write(pickle.dumps(integer_contents))

	file1.seek(0,0)
	return pickle.load(file1)
	file1.close()
	
update_counter('counter.txt')

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))