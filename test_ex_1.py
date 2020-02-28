import unittest
import random 

class TestEx1(unittest.TestCase):
	def test_simple(self, test_function):
		print("0 case:")
		self.assertEqual(test_function(0), "zero")
		print("SUCCESSFUL")
		print("----------")

		print("9 case:")
		self.assertEqual(test_function(9), "nine")
		print("SUCCESSFUL")
		print("----------")

		print("10 case:")
		self.assertEqual(test_function(10), "ten")
		print("SUCCESSFUL")
		print("----------")

		print("11 case:")
		self.assertEqual(test_function(11), "eleven")
		print("SUCCESSFUL")
		print("----------")

		print("20 case:")
		self.assertEqual(test_function(20), "twenty")
		print("SUCCESSFUL")
		print("----------")

		print("55 case:")
		self.assertEqual(test_function(55), "fifty five")
		print("SUCCESSFUL")
		print("----------")

		print("99 case:")
		self.assertEqual(test_function(99), "ninety nine")
		print("SUCCESSFUL")
		print("----------")

		print("100 case:")
		self.assertEqual(test_function(100), "one hundred")
		print("SUCCESSFUL")
		print("----------")

		print("101 case:")
		self.assertEqual(test_function(101), "one hundred one")
		print("SUCCESSFUL")
		print("----------")

		print("999 case:")
		self.assertEqual(test_function(999), "nine hundred ninety nine")
		print("SUCCESSFUL")
		print("----------")

		print("1000 case:")
		self.assertEqual(test_function(1000), "one thousand")
		print("SUCCESSFUL")
		print("----------")

		print("1001 case:")
		self.assertEqual(test_function(1001), "one thousand one")
		print("SUCCESSFUL")
		print("----------")

		print("999999 case:")
		self.assertEqual(test_function(999999), "nine hundred ninety nine thousand nine hundred ninety nine")
		print("SUCCESSFUL")
		print("----------")

		print("1000000 case:")
		self.assertEqual(test_function(1000000), "one million")
		print("SUCCESSFUL")
		print("----------")

		print("1000001 case:")
		self.assertEqual(test_function(1000001), "one million one")
		print("SUCCESSFUL")
		print("----------")

		print("999999999 case:")
		self.assertEqual(test_function(999999999), "nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine")
		print("SUCCESSFUL")
		print("----------")

		print("1000000000 case:")
		self.assertEqual(test_function(1000000000), "one billion")
		print("SUCCESSFUL")
		print("----------")

		print("1000000001 case:")
		self.assertEqual(test_function(1000000001), "one billion one")
		print("SUCCESSFUL")
		print("----------")


		
	def test_random(self, test_function):
		for x in range(1, 21):
			if x in range(1, 6):
				print("Test Number (hundreds):", x)
				r = random.randrange(0, 999, 1)
				print(r, "case:")
				print(test_function(r), "\n")
			if x in range(6, 11):
				print("Test Number (thousands):", x)
				r = random.randrange(1000, 999999, 1)
				print(r, "case:")
				print(test_function(r), "\n")
			if x in range(11, 16):
				print("Test Number (millions):", x)
				r = random.randrange(1000000, 999999999, 1)
				print(r, "case:")
				print(test_function(r), "\n")
			if x in range(16, 21):
				print("Test Number (billions):", x)
				r = random.randrange(1000000000, 999999999999, 1)
				print(r, "case:")
				print(test_function(r), "\n")
			