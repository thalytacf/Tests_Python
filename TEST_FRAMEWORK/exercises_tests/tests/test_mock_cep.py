from unittest import TestCase
from unittest.mock import Mock, patch

from exercicios_testes_unitarios.run import consulta_api_viacep

class TestMock(TestCase):

    @patch('run.print')
    def test_medoto_print(self, mock_print):
    #action
        consulta = consulta_api_viacep()
    #assertions
        self.assertEqual(consulta, 'Cep consultado com sucesso')

