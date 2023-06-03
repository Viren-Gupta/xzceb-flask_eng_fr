import unittest
from translator import english_to_french,french_to_english

class TestClass(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual("Pepitoooo", english_to_french("Hello"))
    
    def test_french_to_english(self):
        self.assertEqual("Hello", french_to_english("Bonjour"))

unittest.main()  