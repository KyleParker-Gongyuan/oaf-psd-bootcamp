import unittest
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
	def test_is_prime(self):
		self.assertTrue(is_prime(2))
		self.assertTrue(is_prime(3))
		self.assertTrue(is_prime(5))
		self.assertTrue(is_prime(7))
		self.assertTrue(is_prime(11))
		self.assertTrue(is_prime(13))
		self.assertTrue(is_prime(17))
		self.assertTrue(is_prime(19))
		self.assertTrue(is_prime(23))
		self.assertTrue(is_prime(29))
		self.assertTrue(is_prime(31))

		self.assertFalse(is_prime(0))
		self.assertFalse(is_prime(1))
		self.assertFalse(is_prime(4))
		self.assertFalse(is_prime(6))
		self.assertFalse(is_prime(8))
		self.assertFalse(is_prime(9))
		self.assertFalse(is_prime(10))
		self.assertFalse(is_prime(15))
		self.assertFalse(is_prime(20))
		self.assertFalse(is_prime(25))
		self.assertFalse(is_prime(30))
		print("Completed Test")

if __name__ == "__main__":
	unittest.main()
