import unittest
from unittest import TestCase
from TEST_FRAMEWORK.unit_test import soma, subtracao, Carro


class TestWithFramework(TestCase):

    def test_soma(self):
        #Arrange

        #Action
        res = soma(2,2)
        #Assertion
        self.assertEqual(res,4,'soma errada')
        self.assertIsInstance(soma(2,2), int)
       #Users\900163\Desktop\Git\PythonHBSIS\TEST_FRAMEWORK

    def test_sub(self):
        pass


    def test_car(self):
        pass
