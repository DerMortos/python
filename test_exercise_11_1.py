import unittest
from exercise_11_1 import city_country

class NamesTestCase(unittest.TestCase):

	def test_location(self):
		location = city_country('santiago', 'chile')
		self.assertEqual(location, 'Santiago, Chile')


unittest.main()