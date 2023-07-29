from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request

import chromedriver_binary  
# He encontrado esta libreria que realiza la descarga y la instalación del driver de Chrome

def descargar_vinetas(num_vinetas):
    # Inicializar el controlador del navegador
    driver = webdriver.Chrome()

    # Abrir la página xkcd.com
    driver.get('https://xkcd.com')

    # Hacer clic en el botón "Random" para obtener la primera viñeta
    # Las clase By define el modo en el que queremos buscar el elemento en el HTML
    random_button = driver.find_element(By.LINK_TEXT, 'Random')
    random_button.click()

    # Esperar un segundo para asegurarse de que la nueva página se haya cargado completamente
    time.sleep(1)

    # Descargar las viñetas solicitadas
    for i in range(num_vinetas):
        # Obtener el enlace de la imagen actual
        image = driver.find_element(By.CSS_SELECTOR, '#comic img')
        image_url = image.get_attribute('src')

        # Descargo la imagen en el cwd
        image_path = f'viñeta_{i+1}.png'
        urllib.request.urlretrieve(image_url, image_path)
        print(f'Descargada la viñeta {i+1}')

        # Hacer clic en el botón "Random" para obtener la siguiente viñeta
        random_button = driver.find_element(By.LINK_TEXT, 'Random')
        random_button.click()

        # Esperar un segundo entre cada descarga
        time.sleep(1)

    # Cerrar el controlador del navegador
    driver.quit()

if __name__ == "__main__":
    num_vinetas = 5
    descargar_vinetas(num_vinetas)
