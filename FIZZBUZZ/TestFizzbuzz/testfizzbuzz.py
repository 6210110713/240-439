from unittest import result
from FIZZANDBUZZ.FIZZBUZZ import FIZZBUZZ

import unittest

class FizzTest(unittest.TestCase):
    def test_give_3_should_Fizz(self):
        number = 3
        result = FIZZBUZZ(number)
        self.assertEqual(result,"Fizz")
    def test_give_5_should_Buzz(self):
        number = 5
        result = FIZZBUZZ(number)
        self.assertEqual(result,"Buzz")
    def test_give_9_should_Fizz(self):
        number = 9
        result = FIZZBUZZ(number)
        self.assertEqual(result,"Fizz")
    def test_give_15_should_Buzz(self):
        number = 15
        result = FIZZBUZZ(number)
        self.assertEqual(result,"FizzBuzz")
    def test_give_5_should_Fizz(self):
        number = -5
        result = FIZZBUZZ(number)
        self.assertEqual(result,"Buzz")
    def test_give_30_should_Buzz(self):
        number = 30
        result = FIZZBUZZ(number)
        self.assertEqual(result,"Buzz")