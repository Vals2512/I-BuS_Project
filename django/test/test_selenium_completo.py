import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestIBuSCompleto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar opciones de Chrome
        options = Options()
        # Puedes descomentar la siguiente línea si deseas ejecutar en segundo plano (sin abrir ventana gráfica)
        # options.add_argument('--headless')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(5)
        cls.base_url = "http://localhost:8000"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_registro_y_flujo_usuario_general(self):
        print("\n=== Iniciando Prueba: Flujo de Usuario General ===")
        driver = self.driver
        
        # 1. Ir a la página de registro
        driver.get(f"{self.base_url}/registrar/")
        self.assertIn("Registro", driver.title)
        print("[OK] Accedió a la página de registro")

        # 2. Registrar un nuevo usuario de prueba
        email_prueba = "usuario_test@ibus.com"
        pass_prueba = "clave123"

        driver.find_element(By.NAME, "email").send_keys(email_prueba)
        driver.find_element(By.NAME, "contrasena").send_keys(pass_prueba)
        driver.find_element(By.NAME, "confirmar_contrasena").send_keys(pass_prueba)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        # Verificar mensaje de éxito
        mensaje_alerta = driver.find_element(By.CLASS_NAME, "alert-success").text
        self.assertIn("registrado correctamente", mensaje_alerta)
        print(f"[OK] Registro exitoso para el usuario: {email_prueba}")

        # 3. Hacer Login con el nuevo usuario
        driver.get(self.base_url)
        driver.find_element(By.NAME, "email").send_keys(email_prueba)
        driver.find_element(By.NAME, "contrasena").send_keys(pass_prueba)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        self.assertIn("usuario/dashboard", driver.current_url)
        print("[OK] Login exitoso de usuario general, redirigido a panel")

        # 4. Navegar por el menú lateral (hacer click en botones y verificar que se activen las secciones)
        btn_empresas = driver.find_element(By.ID, "btn-empresas")
        btn_empresas.click()
        time.sleep(0.5)
        seccion_empresas = driver.find_element(By.ID, "contenido-empresas")
        self.assertTrue(seccion_empresas.is_displayed())
        print("[OK] Visualización correcta de Empresas en menú")

        btn_rutas = driver.find_element(By.ID, "btn-rutas")
        btn_rutas.click()
        time.sleep(0.5)
        seccion_rutas = driver.find_element(By.ID, "contenido-rutas")
        self.assertTrue(seccion_rutas.is_displayed())
        print("[OK] Visualización correcta de Rutas en menú")

        # 5. Ir a Actualizar Cuenta y cambiar email
        nuevo_email = "usuario_test_editado@ibus.com"
        driver.find_element(By.LINK_TEXT, "Actualizar Cuenta").click()
        time.sleep(1)
        self.assertIn("actualizar", driver.current_url)

        email_input = driver.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys(nuevo_email)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        print(f"[OK] Correo actualizado a {nuevo_email}")

        # 6. Eliminar cuenta
        driver.find_element(By.LINK_TEXT, "Eliminar Cuenta").click()
        time.sleep(1)
        self.assertIn("eliminar", driver.current_url)
        
        # Confirmar eliminación
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        # Debería redirigir a Login
        self.assertEqual(driver.current_url.rstrip("/"), self.base_url)
        print("[OK] Cuenta eliminada y redirigido a login")

    def test_02_flujo_administrador_gestion_empresas(self):
        print("\n=== Iniciando Prueba: Flujo de Administrador ===")
        driver = self.driver

        # 1. Iniciar sesión como administrador
        driver.get(self.base_url)
        driver.find_element(By.NAME, "email").send_keys("admin@ibus.com")
        driver.find_element(By.NAME, "contrasena").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1.5)

        self.assertTrue("admin" in driver.current_url or "dashboard" in driver.current_url)
        print("[OK] Login de administrador exitoso")

        # 2. Navegar a Empresas
        driver.get(f"{self.base_url}/empresas/")
        self.assertIn("Empresas registradas", driver.page_source)
        print("[OK] Acceso a lista de empresas")

        # 3. Crear nueva empresa
        driver.find_element(By.LINK_TEXT, "Nueva Empresa").click()
        time.sleep(1)

        # Rellenar formulario
        nombre_empresa = "Empresa de Prueba Selenium"
        driver.find_element(By.NAME, "nombreEmpresa").send_keys(nombre_empresa)
        driver.find_element(By.NAME, "anioFundacion").send_keys("2015")
        driver.find_element(By.NAME, "direccion").send_keys("Calle 100 # 15-30")
        driver.find_element(By.NAME, "telefono").send_keys("3001234567")
        driver.find_element(By.NAME, "cantBuses").send_keys("15")
        driver.find_element(By.NAME, "cantConductores").send_keys("20")

        # Guardar
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        # Verificar que se creó y aparece en la lista
        self.assertIn(nombre_empresa, driver.page_source)
        print(f"[OK] Empresa '{nombre_empresa}' creada correctamente")

        # 4. Editar empresa creada
        # Buscar el botón Editar correspondiente a nuestra empresa de prueba
        filas = driver.find_elements(By.XPATH, "//table/tbody/tr")
        fila_encontrada = None
        for fila in filas:
            if nombre_empresa in fila.text:
                fila_encontrada = fila
                break

        self.assertIsNotNone(fila_encontrada, "No se encontró la empresa de prueba en la tabla.")
        btn_editar = fila_encontrada.find_element(By.LINK_TEXT, "Editar")
        btn_editar.click()
        time.sleep(1)

        # Modificar campo nombre
        nombre_empresa_editada = "Empresa de Prueba Selenium Editada"
        input_nombre = driver.find_element(By.NAME, "nombreEmpresa")
        input_nombre.clear()
        input_nombre.send_keys(nombre_empresa_editada)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        # Verificar edición
        self.assertIn(nombre_empresa_editada, driver.page_source)
        print(f"[OK] Empresa editada con éxito a '{nombre_empresa_editada}'")

        # 5. Eliminar la empresa creada
        filas = driver.find_elements(By.XPATH, "//table/tbody/tr")
        fila_encontrada = None
        for fila in filas:
            if nombre_empresa_editada in fila.text:
                fila_encontrada = fila
                break

        self.assertIsNotNone(fila_encontrada, "No se encontró la empresa editada en la tabla.")
        btn_eliminar = fila_encontrada.find_element(By.LINK_TEXT, "Eliminar")
        btn_eliminar.click()
        time.sleep(1)

        # Confirmar eliminación
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        # Verificar que ya no está
        self.assertNotIn(nombre_empresa_editada, driver.page_source)
        print(f"[OK] Empresa '{nombre_empresa_editada}' eliminada correctamente")

        # 6. Logout
        driver.get(f"{self.base_url}/logout/")
        time.sleep(1)
        self.assertEqual(driver.current_url.rstrip("/"), self.base_url)
        print("[OK] Cierre de sesión de administrador correcto")

if __name__ == "__main__":
    unittest.main()
