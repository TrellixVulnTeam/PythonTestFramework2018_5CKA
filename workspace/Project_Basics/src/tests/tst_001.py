# -*- coding: utf-8 -*-
import unittest
from src.pages.Google import Inicio
from selenium.webdriver.common.keys import Keys
from src.utils.functions import CommonFunctions as Selenium

import allure
import pytest

@allure.feature(u'Google')
@allure.story(u'001: verify query results for RAET in google')
@allure.testcase(u"Caso de Prueba 00001", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""The PO gives us the following specification:</br>
We want to look for “RAET” word in google main page and check if amount of results is bigger than 100000  </br>

1- Access to https://www.google.com. </br>
2- Set RAET in the google textbox. </br>
3- Verify query results under to 10.000. </br>
 </br></br>""")

class tst_001(unittest.TestCase, Selenium):

 
    def setUp(self):
        #ABRIR LA APP
        with allure.step(u'PASO 1: Ingresar a Google'):
            self.driver = self.abrirNavegador(u"https://www.google.com")
        
        #DATOS DESDE EXCEL
        self.user = self.LeerCelda("D2")
        self.passWord = self.LeerCelda("E2")
        
    def test_01(self):
        #ESPERAR EL INICIO DE LA APP
        with allure.step(u'PASO 2: Ingresar Raet como termino de Busqueda'):
            Validar = self.esperar_Xpath(Inicio.img_Logo_xpath)
            if Validar == False:
                self.capturar_Pantalla(u"No se inicializo google.com")
                pytest.skip("No se inicializo google.com")
            
            self.Xpath_elements(Inicio.txt_busqueda_xpath).click()
            self.Xpath_elements(Inicio.txt_busqueda_xpath).send_keys(u"Raet")
            self.capturar_Pantalla(u"Ingresar Raet como termino de Busqueda")
            self.Xpath_elements(Inicio.txt_busqueda_xpath).send_keys(Keys.ENTER)
            self.waitElementIsLoad(Inicio.txt_resultStats_xpath)
            
        with allure.step(u'PASO 3: Verificar los resultados de busqueda'):    
            
            self.capturar_Pantalla(u"Ingresar Raet como termino de Busqueda")
            Resultados = self.Xpath_elements(Inicio.txt_resultStats_xpath).text
            print (Resultados)
            
            RAET = Resultados.split(" ")[2]
            print ("RAET obtuvo: " + str(RAET) + " Resultados de busqueda")
            
        with allure.step(u'PASO 4: Validar que los resultados sean sobre los 10mil'):      
            
            Resultado = RAET.replace(".", "")
            self.assertTrue(int(Resultado) > 10000)
            
            
    def tearDown(self):
        with allure.step(u'PASO 3: Salir de la aplicación.'):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()