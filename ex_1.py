"""
Exercise 1
Created By: Colton Anderson

developed on Linux using python version 3.7.4
"""

import sys
import os
from test_ex_1 import TestEx1

def main():
	in_string = ""
	if len(sys.argv) == 1:
		in_string = input("No command line input found!\n\nPlease enter a number to covert or enter \"test\" to run test cases: ")
	else:
		in_string = sys.argv[1]

	if in_string.lower() == "test":
		'''
		Unit Tests for Generate Algorithm
		'''
		test = TestEx1()

		print("TESTING (simple cases):\n-----------------------\n")
		test.test_simple(generate_words)
		print("\nSUCCESSFULL\n\n")

		print("TESTING (random cases):\n-----------------------\n")
		test.test_random(generate_words)
		print("\nTEST COMPLETE, verify random outputs\n\n")

	else:
		out_string = generate_words(int(in_string))
		print(out_string)

def generate_words(num):
	"""
	Recursive Algorithm for generating word representation from number value
	---------
	INPUT: 
		num: [int] number to transform
	---------
	OUTPUT:
		ret: [string] concatenated string of number representations 
			and place value identifiers
	"""

	ones_and_teens = {
		1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
		10: "ten",
		11: "eleven",
		12: "twelve",
		13: "thirteen",
		14: "fourteen",
		15: "fifteen",
		16: "sixteen",
		17: "seventeen",
		18: "eighteen",
		19: "nineteen",
	}

	tens = {
		20: "twenty ",
		30: "thirty ",
		40: "fourty ",
		50: "fifty ",
		60: "sixty ",
		70: "seventy ",
		80: "eighty ",
		90: "ninety ",
	}

	large_nums = [
		100,
		1000,
		1000000,
		1000000000,
	]

	large_words = [
		" hundred ",
		" thousand ",
		" million ",
		" billion ",
	]
	
	# base case for 0
	if num == 0:
		return "zero"

	# recursive end case for numbers 1-99
	if num < 100: 
		ones_place = num % 10
		tens_place = num % 100 - ones_place

		# case for numbers 10-19 (or "" for zero)
		if tens_place == 10:
			return ones_and_teens.get(num % 100, "")

		# two part return either 1-9 or 20-99 (or "" for zero)
		ret = tens.get(tens_place, "") + ones_and_teens.get(ones_place, "")
		
		ret = ret.strip()
		return ret
	
	place_string = "" # largest place descriptor for value
	place_val = 0

	# loop through large_nums array of values, find largest mulitple of 10 for "thousands" etc.
	for k in range(0, len(large_nums)):
		if large_nums[k] <= num:
			place_string = large_words[k]
			place_val = large_nums[k]
	
	# build recursively generated concatenated string to return to main
	ret = generate_words(int(num / place_val)) + place_string + generate_words(num % place_val)

	# chop off the extraneous zero in some cases (e.g 12345700)
	if ret[-4:] == "zero":
		ret = ret[:-4]

	ret = ret.strip()
	return ret

if __name__ == "__main__":
	main()