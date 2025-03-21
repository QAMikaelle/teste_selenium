# This Python script is using the Selenium WebDriver to automate testing scenarios on a login page.
# Here's a breakdown of what the script is doing:
# This Python script is using the Selenium WebDriver to automate testing scenarios on a login page.
# Here's a breakdown of what the script is doing:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # Acessar a página de login
    driver.get("https://www.hml.lector.live/testesautomatizados/subscribe/login")

    # Esperar até que o campo de username esteja presente
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_username"))
    )
    # Preencher o e-mail errado
    username.send_keys("kasokaosk")

    # Preencher a senha
    password = driver.find_element(By.ID, "login_password")
    password.send_keys("123")

    # Clicar no botão "Entrar"
    login_button = driver.find_element(By.ID, "btn-entrar")
    login_button.click()

    # Verificar a mensagem de erro
    mensagem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".message"))
    )
    assert mensagem.text == "Usuário ou senha inválidos"
    print("Teste realizado com sucesso!")

except Exception as e:
    print(f"Erro: {e}")
    time.sleep(10)

try:
    # Acessar a página de login
    driver.get("https://www.hml.lector.live/testesautomatizados/subscribe/login")

    # Esperar até que o campo de username esteja presente
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_username"))
    )
    # Preencher o e-mail certo
    username.send_keys("qualidade@lectortec.com.br")

    # Preencher a senha errada
    password = driver.find_element(By.ID, "login_password")
    password.send_keys("123456")

    # Clicar no botão "Entrar"
    login_button = driver.find_element(By.ID, "btn-entrar")
    login_button.click()

    # Verificar a mensagem de erro
    mensagem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".message"))
    )
    assert mensagem.text == "Usuário ou senha inválidos"
    print("Teste realizado com sucesso!")

except Exception as e:
    print(f"Erro: {e}")
    time.sleep(10)

try:
    # Acessar a página de login
    driver.get("https://www.hml.lector.live/testesautomatizados/subscribe/login")

    # Esperar até que o campo de username esteja presente
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_username"))
    )
    # Preencher o e-mail certo
    username.send_keys("qualidade@lectortec.com.br")

    # Preencher a senha
    password = driver.find_element(By.ID, "login_password")
    password.send_keys("123")

    # Clicar no botão "Entrar"
    login_button = driver.find_element(By.ID, "btn-entrar")
    login_button.click()
    time.sleep(10)

    print("Teste realizado com sucesso!")

except Exception as e:
    print(f"Erro: {e}")
    time.sleep(10)


finally:
    driver.quit()
