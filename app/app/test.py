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
        """test substract"""
        res = calc.substract(10, 15)

        self.assertEqual(res, 0)
