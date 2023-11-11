import unittest
from app.models.animal import Animal
from app.models.enclosure import Enclosure
from app.models.visitors import Visitor
from app.models.player import Player
from app.models.zoo import Zoo
from appp import Appp  

class TestAppp(unittest.TestCase):

    def setUp(self):
        """Este método é chamado antes de cada teste."""
        self.app = Appp()

    def test_add_animal_to_enclosure(self):
        self.app.add_animal_to_enclosure()
        self.assertEqual(len(self.app.lion_enclosure.animals), 1)
        self.assertIsInstance(self.app.lion_enclosure.animals[0], Animal)

    def test_feed_animal(self):
        initial_happiness = self.app.animal.happiness_level
        self.app.feed_animal()
        self.assertEqual(self.app.animal.happiness_level, initial_happiness + 50)

    def test_add_enclosure_to_zoo(self):
        self.app.add_enclosure_to_zoo()
        self.assertEqual(len(self.app.zoo.enclosures), 1)
        self.assertIsInstance(self.app.zoo.enclosures[0], Enclosure)

    def test_cuidar_bem_recinto(self):
        self.app.cuidar_bem_recinto()
        self.assertTrue(self.app.lion_enclosure.well_maintained)

    def test_insert_visitor(self):
        initial_visitor_count = len(self.app.zoo.visitors)
        self.app.insert_visitor()
        self.assertEqual(len(self.app.zoo.visitors), initial_visitor_count + 1)
        self.assertIsInstance(self.app.zoo.visitors[-1], Visitor)

    def test_cuidar_mal_recinto(self):
        self.app.cuidar_mal_recinto()
        self.assertFalse(self.app.lion_enclosure.well_maintained)

    def test_get_an_animal_felicidade(self):
        self.app.animal.happiness_level = 60  # Configurar um nível de felicidade garantido para ser feliz
        felicidade = self.app.get_an_animal_felicidade()
        self.assertTrue(felicidade)

    def test_ganhar_dinheiro(self):
        initial_money = self.app.player.money
        self.app.zoo.add_visitor(Visitor("Visitante", 100))  # Adicionando um visitante para garantir alguma receita
        self.app.ganhar_dinheiro()
        self.assertGreater(self.app.player.money, initial_money)


if __name__ == '__main__':
    unittest.main()

# class TestApppp(unittest.TestCase):

#     def test_create_animal(self):
#         app_instance = Appp()

#         animal = app_instance.create_animal()

#         self.assertIsNotNone(animal)
#         self.assertEqual(animal.name, "Simba")
#         self.assertEqual(animal.species, "Leão")

#     def test_feed_animal(self):
#         app_instance = Appp()
#         hApppiness_level = app_instance.feed_animal()
#         self.assertEqual(hApppiness_level, 100)  

#     def test_criar_recinto(self):
#         app_instance = Appp()
#         enclosure = app_instance.criar_recinto()
#         self.assertIsNotNone(enclosure)
#         self.assertEqual(enclosure.name, "Savana Africana")
#         self.assertEqual(enclosure.species, "Leão")

#     def test_cuidar_bem_recinto(self):
#         app_instance = Appp()
#         enclosure = app_instance.cuidar_bem_recinto()
#         self.assertIsNotNone(enclosure)
#         self.assertTrue(enclosure.well_maintained)

#     def test_cuidar_mal_recinto(self):
#         app_instance = Appp()
#         enclosure = app_instance.cuidar_mal_recinto()
#         self.assertIsNotNone(enclosure)
#         self.assertFalse(enclosure.well_maintained)

#     def test_get_an_animal_felicidade(self):
#         app_instance = Appp()
#         felicidade = app_instance.get_an_animal_felicidade()
#         self.assertTrue(felicidade)
       

#     def test_ganhar_dinheiro(self):
#         app_instance = Appp()
       
#         money_earned = app_instance.ganhar_dinheiro()
#         self.assertIsNotNone(money_earned)
    

# if __name__ == '__main__':
#     unittest.main()
