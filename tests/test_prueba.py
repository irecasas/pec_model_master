from pec_pipelines.prueba import hola
from unittest import TestCase

class TestPEC(TestCase):
    def test_hola(self):
        saludo = hola()
        assert saludo == 'HOLA'
