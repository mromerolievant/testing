from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configurar Selenium con el navegador
driver = webdriver.Chrome()  # o el navegador que uses
driver.get("https://app.smartdbi.com/dashboard")
try:
    # Encuentra el campo de texto por su ID
    text_field = driver.find_element(By.ID,"f-username")  # Reemplaza "text_field_id" por el ID del elemento real 
    # Escribe en el campo de texto
    text_field.click()
    text_field.send_keys("miguelromero@lievant.com")
    text_password = driver.find_element(By.ID,"f-password")
    text_password.click()
    text_password.send_keys("Isabella4231")
    boton_login = driver.find_element(By.ID,"login")
    boton_login.click()
    time.sleep(40)
    try:
        boton_dashboard = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".SideNavListItem__ListItemText-fxnpQU kUCCJP"))
        )
        boton_dashboard.click()
    except Exception as r:
        print(f"El error es no se por que no carga: {r}")
        
        print("Texto escrito con éxito.")
except Exception as e:
    print(f"Error al escribir en el campo de texto: {e}")
    time.sleep(10)

driver.quit()
