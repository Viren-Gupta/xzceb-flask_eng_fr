import unittest
from translator import english_to_french,french_to_english

class TestClass(unittest.TestCase):
    def test_english_to_french_equal(self):
        self.assertEqual("Pepitoooo", english_to_french("Hello"))
    def test_english_to_french_not_equal(self):
        self.assertNotEqual("Xyz", english_to_french("Hello"))
    def test_french_to_english_equal(self):
        self.assertEqual("Hello", french_to_english("Bonjour"))
    def test_french_to_english_not_equal(self):
        self.assertNotEqual("Hello1", french_to_english("Bonjour"))
        

unittest.main()  