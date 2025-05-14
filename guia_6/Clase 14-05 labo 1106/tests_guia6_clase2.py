import unittest
from guia6_clase2 import *

class test_volumen(unittest.TestCase):
    #se pueden definir los casos por separado
    def test_volumen_1(self):
        self.assertAlmostEqual(volumen_esfera(1.0), 4.1866666666666665, places=4)

    def test_volumen_nulo(self):
        self.assertAlmostEqual(volumen_esfera(0.0), 0.0, places=1)

    def test_volumen_5_25(self):
        self.assertAlmostEqual(volumen_esfera(5.25), 605.82375, places=5)
     
        
class test_triada_pitagorica(unittest.TestCase):
    def test_triada_verdadera_correcta(self):
        self.assertTrue(triada_pitagorica(3,4,5))

    def test_triada_falsa(self):
        self.assertFalse(triada_pitagorica(1,7,9))

    def test_triada_ok_desordenada(self):
        self.assertFalse(triada_pitagorica(5,4,3))

class test_es_multiplo_de(unittest.TestCase):
    def test_es_multiplo_cero_y_uno(self):
        self.assertTrue(es_multiplo_de(0,5))
        self.assertFalse(es_multiplo_de(1,5))
        self.assertTrue(es_multiplo_de(15,1))
    
    def test_es_multiplo_valores_iguales(self):
        self.assertTrue(es_multiplo_de(8,8))
        self.assertEqual(es_multiplo_de(12,12),True)
        
    def test_es_multiplo_valores_distintos(self):
        self.assertTrue(es_multiplo_de(8,2))
        self.assertFalse(es_multiplo_de(3,2))
        
class test_devolver_el_doble(unittest.TestCase):
    def test_devolver_el_doble_cero_uno(self):
        self.assertEqual(devolver_el_doble_si_es_par(0),0)
        self.assertEqual(devolver_el_doble_si_es_par(1),1)
        
    def test_devolver_el_doble_numero_par(self):
        self.assertEqual(devolver_el_doble_si_es_par(2),4)
        self.assertEqual(devolver_el_doble_si_es_par(10),20)
        
    def test_devolver_el_doble_numero_impar(self):
        self.assertEqual(devolver_el_doble_si_es_par(3),3)
        self.assertEqual(devolver_el_doble_si_es_par(11), 11)
    
class test_farenheit_a_celcius(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(farenheit_a_celcius(140.0),60.0)
        self.assertNotAlmostEqual(farenheit_a_celcius(140.0),60.5)
          
class test_es_primo(unittest.TestCase):
    def test_uno_y_cero(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(1))
        
    def test_primo(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(17))
        
    def test_compuesto(self):
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(964))
        
    def test_negativo(self):
        self.assertTrue(es_primo(-2))
        self.assertTrue(es_primo(-17))
        self.assertFalse(es_primo(-4))
        self.assertFalse(es_primo(-964))
        
class test_cuantos_primos_en_rango(unittest.TestCase):
    def test_n_menor_m(self):
        self.assertEqual(cuantos_primos_en_rango(2,7),4)
        
    def test_n_igual_m(self):
        self.assertEqual(cuantos_primos_en_rango(5,5),1)
        self.assertEqual(cuantos_primos_en_rango(4,4),0)
    
    def test_n_mayor_m(self):
        self.assertEqual(cuantos_primos_en_rango(7,2),4)
    
    def test_n_pos_m_neg(self):
        self.assertEqual(cuantos_primos_en_rango(-3,3),4)
        
    def test_m_pos_n_neg(self):
        self.assertEqual(cuantos_primos_en_rango(3,-3),4)
        
        

if __name__ == '__main__':
    unittest.main() 
