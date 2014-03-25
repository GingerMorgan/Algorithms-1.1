import minmax
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        input = [1,2,3,4,5]
        expMin = 1
        assert minmax.mini(input) == expMin #Test 1 Fails

    def test2(self):
        input = [2,3,4,5,6]
        expMin = 2
        assert minmax.mini(input) == expMin #Test 2 Fails
   
   
if __name__ == '__main__':
    unittest.main()