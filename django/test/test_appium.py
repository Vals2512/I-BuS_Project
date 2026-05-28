import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.browser_name = 'Chrome'
options.set_capability('appium:uiautomator2ServerLaunchTimeout', 60000)
options.set_capability('appium:uiautomator2ServerInstallTimeout', 60000)
print("Conectando con el servidor de Appium...")
driver = webdriver.Remote('http://localhost:4723', options=options)

try:
    print("Abriendo I-BuS desde Chrome Mobile en el Emulador...")
    driver.get('http://10.0.2.2:8000/')
    time.sleep(3)

    print("Ejecutando Prueba APPIUM-01: Login responsivo...")
    email_field = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
    email_field.click()
    email_field.clear()
    email_field.send_keys('admin@ibus.com')
    
    pass_field = driver.find_element(By.CSS_SELECTOR, '[name="contrasena"]')
    pass_field.click()
    pass_field.clear()
    pass_field.send_keys('admin123')
    pass_field.submit()
    
    # Esperar a que la URL cambie tras el login (hasta 10 segundos)
    logged_in = False
    for _ in range(10):
        if 'dashboard' in driver.current_url or 'admin' in driver.current_url:
            logged_in = True
            break
        time.sleep(1)
        
    if not logged_in:
        print(f"DEBUG APPIUM-01: URL actual = {driver.current_url}")
        print(f"DEBUG APPIUM-01: Page Source = {driver.page_source[:2000]}")
    assert logged_in, f"El login fallo o no redirigio a tiempo. URL actual: {driver.current_url}"
    print('[OK] APPIUM-01 PASA: Login exitoso y redireccion responsiva correcta.')

    print("Ejecutando Prueba APPIUM-02: CRUD de Barrios en Vista Móvil...")
    # Ir a la lista de barrios
    driver.get('http://10.0.2.2:8000/barrios/')
    time.sleep(2)
    self_page_source = driver.page_source
    
    # Agregar barrio
    driver.find_element(By.LINK_TEXT, 'Agregar Barrio').click()
    time.sleep(2)
    
    barrio_nombre = "Barrio Appium"
    input_field = driver.find_element(By.CSS_SELECTOR, '[name="nombreBarrio"]')
    input_field.click()
    input_field.clear()
    input_field.send_keys(barrio_nombre)
    input_field.submit()
    
    # Esperar a que el barrio aparezca en la pagina (hasta 10 segundos)
    found = False
    for _ in range(10):
        if barrio_nombre in driver.page_source:
            found = True
            break
        time.sleep(1)
        
    if not found:
        print(f"DEBUG APPIUM-02a: URL actual = {driver.current_url}")
        print(f"DEBUG APPIUM-02a: Page Source = {driver.page_source[:2000]}")
    assert found, f"El barrio '{barrio_nombre}' no se encontro en la pagina."
    print(f'[OK] APPIUM-02a: Barrio "{barrio_nombre}" creado exitosamente.')

    # Editar barrio
    filas = driver.find_elements(By.XPATH, "//table/tbody/tr")
    fila_barrio = None
    for fila in filas:
        if barrio_nombre in fila.text:
            fila_barrio = fila
            break
            
    assert fila_barrio is not None, "No se encontró el barrio creado para editar."
    btn_editar = fila_barrio.find_element(By.LINK_TEXT, "Editar")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_editar)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", btn_editar)
    time.sleep(2)
    
    barrio_editado = "Barrio Prueba"
    input_nombre = driver.find_element(By.CSS_SELECTOR, '[name="nombreBarrio"]')
    input_nombre.click()
    input_nombre.clear()
    input_nombre.send_keys(barrio_editado)
    input_nombre.submit()
    
    # Esperar a que el barrio editado aparezca
    found = False
    for _ in range(10):
        if barrio_editado in driver.page_source:
            found = True
            break
        time.sleep(1)
        
    if not found:
        print(f"DEBUG APPIUM-02b: URL actual = {driver.current_url}")
        print(f"DEBUG APPIUM-02b: Page Source = {driver.page_source[:2000]}")
    assert found, f"El barrio editado '{barrio_editado}' no se encontro."
    print(f'[OK] APPIUM-02b: Barrio editado exitosamente a "{barrio_editado}".')

    # Eliminar barrio
    filas = driver.find_elements(By.XPATH, "//table/tbody/tr")
    fila_barrio_editado = None
    for fila in filas:
        if barrio_editado in fila.text:
            fila_barrio_editado = fila
            break
            
    assert fila_barrio_editado is not None, "No se encontró el barrio editado para eliminar."
    btn_eliminar = fila_barrio_editado.find_element(By.LINK_TEXT, "Eliminar")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_eliminar)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", btn_eliminar)
    time.sleep(2)
    
    # Confirmar eliminación
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # Esperar a que el barrio desaparezca
    removed = False
    for _ in range(10):
        if barrio_editado not in driver.page_source:
            removed = True
            break
        time.sleep(1)
        
    if not removed:
        print(f"DEBUG APPIUM-02c: URL actual = {driver.current_url}")
        print(f"DEBUG APPIUM-02c: Page Source = {driver.page_source[:2000]}")
    assert removed, f"El barrio '{barrio_editado}' sigue apareciendo despues de eliminar."
    print('[OK] APPIUM-02c: Barrio eliminado exitosamente.')

    print("Ejecutando Prueba APPIUM-03: Visualización de Estadísticas en Móvil...")
    driver.get('http://10.0.2.2:8000/admin/estadisticas/')
    time.sleep(2)
    
    # Verificar que el canvas del gráfico de empresas esté presente
    canvas_grafico = driver.find_element(By.CSS_SELECTOR, '#graficoEmpresas') 
    assert canvas_grafico is not None
    assert 'Estadísticas de Pasajeros por Ruta' in driver.page_source
    print('[OK] APPIUM-03 PASA: Pagina de estadisticas y graficos cargados correctamente en movil.')

finally:
    driver.quit()
