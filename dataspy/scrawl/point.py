from math import sqrt
import unittest

class Point(object):
    """Point class with hidden x and y attributes (these must be accessed
    using a method)"""

    def __init__(self, s='', x=0, y=0):
        self._s = s
        self._x = x
        self._y = y
        
 
    # access methods
    def get_s(self):
        return self._s

    def get_x(self):
        return self._x
 
    def get_y(self):
        return self._y
 
    def set_s(self, s):
        self._s = s
 
    def set_x(self, x):
        self._x = x
 
    def set_y(self, y):
        self._y = y
 
    def dist(self, p):
        dx = self.get_x() - p.get_x()
        dy = self.get_y() - p.get_y()
        return sqrt(dx*dx + dy*dy)
 
class TestPoint(unittest.TestCase):
 
    def test_dist(self):
        p1 = Point('p1',1,2)
        p2 = Point('p2',5,-1)
        self.assertEqual(p1.dist(p2), 5.0)
 
if __name__ == '__main__':
    unittest.main()
    
