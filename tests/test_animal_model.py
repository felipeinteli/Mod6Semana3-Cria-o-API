import unittest
from app.models.animal_model import Animal

class TestAnimalModel(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("Simba", "Leão", 50)

    def test_animal_creation(self):
        self.assertEqual(self.animal.name, "Simba")
        self.assertEqual(self.animal.species, "Leão")
        self.assertEqual(self.animal.happiness_level, 50)

    # Adicione mais testes relacionados à alimentação e outros métodos

if __name__ == '__main__':
    unittest.main()