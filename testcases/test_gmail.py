import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select    # Para los elementos Select - Dropdown


class TestLogin():
    def test_Gmail(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(url='https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AVQVeyyxR9-FNBpXL5iL4HwGnzi1hPWDWhdU_D-VNK6dPa_DPaTs0A2e7TjeJb72iFrVu09a31WE5&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1442592184%3A1698150008071214&theme=glif')
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='identifierId']").send_keys("testingqammr@gmail.com")
        driver.find_element(By.XPATH, "//span[contains(text(),'Siguiente')]").click()
        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Underc0de")
        driver.find_element(By.XPATH, "//span[contains(text(),'Siguiente')]").click()
        driver.find_element(By.XPATH, "//div[contains(text(),'Compose')]").click()
        driver.find_element(By.XPATH, "//input[@id=':1dd']").click() # Redactar
        driver.find_element(By.XPATH, '//iframe [@name="app"]').click() # Frame Redactar
        driver.find_element(By.XPATH, "//input[@id=':c8']").send_keys("testingqammr@gmail.com") # Destino Correo
        driver.find_element(By.XPATH, "//input[@id=':8n']").send_keys("Correo de prueba") # Asunto
        driver.find_element(By.XPATH, "//div[@id=':9w']").send_keys("Correo de correo electrónico de prueba") # Cuerpo correo
        driver.find_element(By.XPATH, "//div[@id=':8d']").click() # Button Senmd
        time.sleep(15)
        driver.find_element(By.XPATH, '//*[id = ":1ae"] / span[alt = "Not starred"]').click()  # Button Senmd





