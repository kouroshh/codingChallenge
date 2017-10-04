import unittest
from test import mySplit

##
# Class that models all the test cases
# The input and output is printed only to show the results, it could be deleted.
##
class Test(unittest.TestCase):

    def test1(self):
        a = [1, 2, 3, 4, 5]
        size = 3
        self.assertEqual(mySplit(a,size), [[1,2],[3,4],[5]])
	print	
	print "Input: " + str(a)
	print "Size: " + str(size)
	print "Output: " + str(mySplit(a,size))
 

    def test2(self):
        a = [1,2,3,4,5,6,7,8,9]
        size = 3
        self.assertEqual(mySplit(a, size), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	print 	
	print "Input: " + str(a)
	print "Size: " + str(size)
	print "Output: " + str(mySplit(a,size))

    def test3(self):
        a = [1, 2, 3, 4, 5]
        size = 0
        self.assertEqual(mySplit(a, size), a)
	print 	
	print "Input: " + str(a)
	print "Size: " + str(size)
	print "Output: " + str(mySplit(a,size))

    def test4(self):
        a = [1, 2, 3]
        size = 3
        self.assertEqual(mySplit(a, size), [[1],[2],[3]])
	print
	print "Input: " + str(a)
	print "Size: " + str(size)
	print "Output: " + str(mySplit(a,size)) 

    def test5(self):
        a = []
        size = 3
        self.assertEqual(mySplit(a, size), a)
	print
	print "Input: " + str(a)
	print "Size: " + str(size)
	print "Output: " + str(mySplit(a,size))

    def test6(self):
        a = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12, 13]
        size = 7
        self.assertEqual(mySplit(a, size), [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13]])
	print
	print "Input: " + str(a)
	print "Size: " + str(size)
	print "Output: " + str(mySplit(a,size))

    def test7(self):
        a = ['a','b','c','d']
        size = 2
        self.assertEqual(mySplit(a, size), [['a', 'b'], ['c', 'd']])
	print
	print "Input: " + str(a)
	print "Size: " + str(size)
	print "Output: " + str(mySplit(a,size))

    def test8(self):
        a = 1
        size = 2
        self.assertEqual(mySplit(a, size), a)
	print 
	print "Input: " + str(a)
	print "Size: " + str(size)
	print "Output: " + str(mySplit(a,size))


if __name__ == '__main__':
    unittest.main()
