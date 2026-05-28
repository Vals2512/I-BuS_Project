import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8000/")
    driver.maximize_window()
    time.sleep(2)

    input_email = driver.find_element(By.NAME, "email")
    input_contrasena = driver.find_element(By.NAME, "contrasena")
    btn_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    input_email.send_keys("admin@ibus.com")
    input_contrasena.send_keys("admin123")
    
    time.sleep(1) 
    btn_submit.click()
    time.sleep(3)

    if "dashboard" in driver.current_url or "/admin/" in driver.current_url:
        print("¡Prueba de Frontend Exitosa! Redirección correcta.")
    else:
        print(f"Fallo en la prueba: No se detectó la redirección esperada.")
        print(f"URL actual: {driver.current_url}")
        try:
            error_msg = driver.find_element(By.CLASS_NAME, "error").text
            print(f"Mensaje de error en pantalla: {error_msg}")
        except Exception:
            try:
                error_msg = driver.find_element(By.XPATH, "//*[contains(@class, 'error') or contains(@class, 'alert')]").text
                print(f"Mensaje de error/alerta: {error_msg}")
            except Exception:
                print("No se encontró ningún elemento de error explícito en la página.")

finally:
    driver.quit()