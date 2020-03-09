from unittest import TestCase
from unittest.mock import Mock, call, patch
from Tests_Python.run import consulta_api_viacep


class TestMock(TestCase):

    @patch('exercicios_testes_unitarios.run.print')
    def test_medoto_print(self, mock_print):
    #action
        mock_print.return_value = '89114456'
        consulta = consulta_api_viacep()
    #assertions
        self.assertEqual(consulta, 'Cep consultado com sucesso!')


    @patch('exercicios_testes_unitarios.run.input', return_value="00000000")
    def test_solicitr_cep_input(self, mock_input):
        mock_input.side_effects = ['00000000']
        res = consulta_api_viacep()
        self.assertEqual(res, 'Cep consultado com sucesso!')
        mock_input.assert_has_calls([call('Informe o cep para consulta: ')])

# restornar um dic {'cep':'', 'logradouro':'', 'complemento':'', 'bairro':'', 'localidade':'', 'uf':'', 'unidade':'', 'ibge':'', 'gia':''}



