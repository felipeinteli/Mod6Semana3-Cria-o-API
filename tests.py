import unittest

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
        self.assertEqual(hApppiness_level, 100)  

    def test_criar_recinto(self):
        app_instance = Appp()
        enclosure = app_instance.criar_recinto()
        self.assertIsNotNone(enclosure)
        self.assertEqual(enclosure.name, "Savana Africana")
        self.assertEqual(enclosure.species, "Leão")

    def test_cuidar_bem_recinto(self):
        app_instance = Appp()
        enclosure = app_instance.cuidar_bem_recinto()
        self.assertIsNotNone(enclosure)
        self.assertTrue(enclosure.well_maintained)

    def test_cuidar_mal_recinto(self):
        app_instance = Appp()
        enclosure = app_instance.cuidar_mal_recinto()
        self.assertIsNotNone(enclosure)
        self.assertFalse(enclosure.well_maintained)

    def test_get_an_animal_felicidade(self):
        app_instance = Appp()
        felicidade = app_instance.get_an_animal_felicidade()
        self.assertTrue(felicidade)
       

    def test_ganhar_dinheiro(self):
        app_instance = Appp()
       
        money_earned = app_instance.ganhar_dinheiro()
        self.assertIsNotNone(money_earned)
    

if __name__ == '__main__':
    unittest.main()
