import unittest
# from Appp import  create_animal, feed_animal, criar_recinto, add_animal_to_enclosure, cuidar_bem_recinto, cuidar_mal_recinto, get_an_animal_felicidade, ganhar_dinheiro
# from Appp.models.animal import Animal
# from Appp.models.enclosure import Enclosure
# from Appp.models.visitors import Visitors
# from Appp.models.player import Player
# from Appp.models.zoo import Zoo
from appp import Appp
class TestApppp(unittest.TestCase):

    def test_create_animal(self):
        app_instance = Appp()

        animal = app_instance.create_animal()

        self.assertIsNotNone(animal)
        self.assertEqual(animal.name, "Simba")
        self.assertEqual(animal.species, "Leão")

    def test_feed_animal(self):
        app_instance = Appp()
        hApppiness_level = app_instance.feed_animal()
        self.assertEqual(hApppiness_level, 50)  

    def test_criar_recinto(self):
        app_instance = Appp()
        enclosure = app_instance.criar_recinto()
        self.assertIsNotNone(enclosure)
        self.assertEqual(enclosure.name, "Savana Africana")
        self.assertEqual(enclosure.species, "Leão")

    def test_add_animal_to_enclosure(self):
        app_instance = Appp()
        enclosure = app_instance.add_animal_to_enclosure()
        self.assertIsNotNone(enclosure)
        self.assertTrue(enclosure.has_animal("Simba"))

    def test_cuidar_bem_recinto(self):
        app_instance = Appp()
        enclosure = app_instance.cuidar_bem_recinto()
        self.assertIsNotNone(enclosure)
        self.assertTrue(enclosure.is_well_maintained)

    def test_cuidar_mal_recinto(self):
        app_instance = Appp()
        enclosure = app_instance.cuidar_mal_recinto()
        self.assertIsNotNone(enclosure)
        self.assertFalse(enclosure.is_well_maintained)

    def test_get_an_animal_felicidade(self):
        app_instance = Appp()
        hApppiness = app_instance.get_an_animal_felicidade()
        self.assertIsNotNone(hApppiness)
        # Add assertions based on expected hApppiness level

    def test_ganhar_dinheiro(self):
        app_instance = Appp()
        # Test the ganhar_dinheiro function
        money_earned = app_instance.ganhar_dinheiro()
        self.assertIsNotNone(money_earned)
        # Add assertions based on expected money earned

if __name__ == '__main__':
    unittest.main()
