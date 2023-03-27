from django.test import SimpleTestCase

import calc



class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """Test adding numbers together"""
        
        res = calc.add(5, 6)

        self.assertEqual(res, 11)