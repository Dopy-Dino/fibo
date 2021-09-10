import unittest
import app

class TestFibo(unittest.TestCase):
    def testZero(self):
        n = 0
        fib = app.fibonacci(n)

        self.assertEqual(fib, 0)
    def testOne(self):
        n = 1
        fib = app.fibonacci(n)

        self.assertEqual(fib, 1)
    def testString(self):
        n = 'a'
        fib = app.fibonacci(n)

        self.assertEqual(fib, 'value can not be converted to integer')
    def testOver(self):
        n = 100001
        fib = app.fibonacci(n)

        self.assertEqual(fib, 'value n better under 100000')
    def testHappyPath(self):
        n = 10
        fib = app.fibonacci(n)

        self.assertEqual(fib, 55)

if __name__ == '__main__':
    unittest.main()