"""
sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test calc"""

    def test_add_numbers(self):
        """test add"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        
        res = calc.substract(5,4)
        self.assertEqual(res, 1)

