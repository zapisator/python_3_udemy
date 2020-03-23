#!/usr/bin/env python3

import unittest
import fizz_buzz

class Fizz_buzz_tests(unittest.TestCase):

	def test_fizz(self):
		nb = 6
		result = fizz_buzz.get_reply(nb)
		self.assertEqual(result, "Fizz")
		return

	def test_buzz(self):
		nb = 10
		result = fizz_buzz.get_reply(nb)
		self.assertEqual(result, "Buzz")
		return

	def test_fizzbuzz(self):
		nb = 15
		result = fizz_buzz.get_reply(nb)
		self.assertEqual(result, "FizzBuzz")
		return

	# def test_nb(self):
	# 	nb = 2
	# 	result = fizz_buzz.get_reply(nb)
	# 	self.assertEqual(result, "Fizz")
	# 	return

if __name__ == '__main__':
	unittest.main()