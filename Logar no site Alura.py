#Instalar no cmd do computador que será utilizado 
#pip install pandas openpyxl selenium

import pandas as pd
import time 

# Caminho do arquivo
caminho_arquivo = r"C:\Users\Ti\Desktop\Projeto x\acesso.xlsx"

# Lê o Excel
df = pd.read_excel(caminho_arquivo, header=None)

# Captura os dados
login = df.iloc[0, 1]
senha = df.iloc[1, 1]
site = df.iloc[2, 1]

#acessar navegador anônimo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#- Desabilitar a automação explícita (ocultar que é Selenium):
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Configura modo anônimo
options = Options()
options.add_argument("--incognito")

# Inicia navegador
driver = webdriver.Chrome(options=options)
driver.get(site)


# Espera o campo de login aparecer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "login-email"))
)

# Localiza os campos - seletor 
#campo_email = driver.find_element(By.ID, "email")
campo_email = driver.find_element(By.ID, "login-email")
time.sleep(5)

#campo_senha = driver.find_element(By.ID, "password")
campo_senha = driver.find_element(By.ID, "password")
time.sleep(5)

print("login capturado: ", login)
print("senha capturada: ", senha)

# Preenche os dados
campo_email.send_keys(login)
time.sleep(5) 
campo_senha.send_keys(senha)
time.sleep(5)

#validar captcha
print("✅ Dados preenchidos. Agora resolva o CAPTCHA manualmente.")
input("🕒 Após marcar a caixa 'Não sou um robô', pressione Enter para continuar...")

# Clica no botão de login depois que você resolver o CAPTCHA
botao_entrar = driver.find_element(By.CLASS_NAME, "btn-login")
botao_entrar.click()

#Verificar se foi feito o login com sucesso
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Espera até que um elemento da página logada esteja presente
    elemento_logado = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "usuario-logado"))
    )
    print("Login bem-sucedido!")
except:
    print("Falha no login.")