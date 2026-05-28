from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
driver = webdriver.Chrome()
driver.get('http://localhost:8000/')  # I-BuS en Docker
 
# Prueba P01: Login con credenciales correctas
driver.find_element(By.NAME, 'email').send_keys('admin@ibus.com')
driver.find_element(By.NAME, 'contrasena').send_keys('admin123')
driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
time.sleep(1)
assert 'dashboard' in driver.current_url or 'admin' in driver.current_url
print(' P01 PASA: Login correcto redirige al admin dashboard')
 
# Prueba P02: Verificar 4 empresas en la tabla
driver.get('http://localhost:8000/empresas/')
filas = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
assert len(filas) == 4
print(f' P02 PASA: Se muestran {len(filas)} empresas')
driver.quit()
