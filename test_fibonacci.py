import unittest
import fibonacci


class fibonacciTestCases(unittest.TestCase):

    def test1(self):
        self.assertEqual(fibonacci.fibo(10),55)
    
    def test2(self):
        self.assertEqual(fibonacci.factorial(5),120)
    
if __name__ == "__main__":
    unittest.main()

