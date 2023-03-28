import unittest
from countries import get_country_code


class CountriesTestCase(unittest.TestCase):

    """Tests for 'countries.py'."""

    def test_get_country_code(self):

        """Does code like 'ad' get returned for 'Andorra'?"""
        self.country_name = 'Andorra'
        self.country_code = 'ad'
        code = get_country_code(self.country_name)
        self.assertEqual(code, self.country_code)


unittest.main()