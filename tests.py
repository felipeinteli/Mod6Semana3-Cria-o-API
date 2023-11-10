import unittest
# from app import  create_animal, feed_animal, criar_recinto, add_animal_to_enclosure, cuidar_bem_recinto, cuidar_mal_recinto, get_an_animal_felicidade, ganhar_dinheiro
# from app.models.animal import Animal
# from app.models.enclosure import Enclosure
# from app.models.visitors import Visitors
# from app.models.player import Player
# from app.models.zoo import Zoo
from app import App
class TestApp(unittest.TestCase):

    def test_create_animal(self):
        app = App()

        animal = app.create_animal()

        self.assertIsNotNone(animal)
        self.assertEqual(animal.name, "Simba")
        self.assertEqual(animal.species, "Leão")

    def test_feed_animal(self):
        app = App()
        happiness_level = app.feed_animal()
        self.assertEqual(happiness_level, 50)  

    def test_criar_recinto(self):
        app = App()
        enclosure = app.criar_recinto()
        self.assertIsNotNone(enclosure)
        self.assertEqual(enclosure.name, "Savana Africana")
        self.assertEqual(enclosure.species, "Leão")

    def test_add_animal_to_enclosure(self):
        app = App()
        enclosure = app.add_animal_to_enclosure()
        self.assertIsNotNone(enclosure)
        self.assertTrue(enclosure.has_animal("Simba"))

    def test_cuidar_bem_recinto(self):
        app = App()
        enclosure = app.cuidar_bem_recinto()
        self.assertIsNotNone(enclosure)
        self.assertTrue(enclosure.is_well_maintained)

    def test_cuidar_mal_recinto(self):
        app = App()
        enclosure = app.cuidar_mal_recinto()
        self.assertIsNotNone(enclosure)
        self.assertFalse(enclosure.is_well_maintained)

    def test_get_an_animal_felicidade(self):
        app = App()
        happiness = app.get_an_animal_felicidade()
        self.assertIsNotNone(happiness)
        # Add assertions based on expected happiness level

    def test_ganhar_dinheiro(self):
        app = App()
        # Test the ganhar_dinheiro function
        money_earned = app.ganhar_dinheiro()
        self.assertIsNotNone(money_earned)
        # Add assertions based on expected money earned

if __name__ == '__main__':
    unittest.main()
