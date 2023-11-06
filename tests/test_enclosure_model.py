import unittest
from app.models.enclosure import Enclosure
from app.models.animal import Animal

class TestEnclosureModel(unittest.TestCase):
    def setUp(self):
        self.enclosure = Enclosure("Savana Africana", "Leão")

    def test_enclosure_creation(self):
        self.assertEqual(self.enclosure.name, "Savana Africana")
        self.assertEqual(self.enclosure.species, "Leão")
        self.assertEqual(self.enclosure.animals, [])
        self.assertEqual(self.enclosure.well_maintained, True)