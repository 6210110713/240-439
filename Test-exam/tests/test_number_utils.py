from coe_number.number_utils import is_prime_list

import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1,2,3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_5_7_11_is_prime(self):
        prime_list = [5,7,11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_2_4_6_is_prime(self):
        prime_list = [2,4,6]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_2_3_0_is_prime(self):
        prime_list = [2,3,0]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_odd_1_2_3_is_prime(self):
        prime_list = [-1,-2,-3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)