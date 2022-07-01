import unittest


# テスト対象のplus関数
def plus(a, b):
    return a + b


# テストプログラム
class TestPlus(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(10, plus(2, 8))

if __name__ == '__main__':
    unittest.main()