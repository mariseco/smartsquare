"""
    provo test
"""
import unittest

from smartsquare.core import square

class TestCore(unittest.TestCase):
    '''Unittest for core module'''
 #scritto in Camel case ovvero prima lettera con maiuscola e si separano le lettere con la maiuscola, invece snake case scrivi tutto minuscolo e separi le parole cone un underscore
    
    def test_float(self):
        '''test with floats'''
        self.assertAlmostEqual(square(2.),4.)
        
if __name__ == "__main__":
    unittest.main()
