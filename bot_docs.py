from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

# Configuração do WebDriver com modo de navegação privada
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')  # Adiciona a opção de navegação privada

driver = webdriver.Chrome(options=chrome_options) 

nomes = ['Ana', 'Carolina', 'Beatriz']
sobrenomes = ['Silva', 'Correa', 'Santos']

coluna_a1 = ['#27 - Fernando Quesada','#28 - Firewing','#29 - Thiago Bianchi','#30 - Angra','#31 - Luis Mariutti & Edu Falaschi','#32 - Torture Squad']

def gerar_email(nome, sobrenome):
    provedores = ['gmail.com', 'hotmail.com']
    nome_formatado = f"{nome.lower()}_{sobrenome.lower()}"
    provedor = random.choice(provedores)
    return f"{nome_formatado}@{provedor}"

# Loop para gerar dados fictícios
for nome in nomes:
    for sobrenome in sobrenomes:
        email = gerar_email(nome, sobrenome)
        print(f"{nome} {sobrenome}: {email}")

        # Encontrar a caixa de texto e inserir o email
        caixa_texto_email = driver.find_element(By.CSS_SELECTOR, 'input[name="E-mail"]')
        caixa_texto_email.clear()  # Limpa qualquer conteúdo existente
        caixa_texto_email.send_keys(email)

        # Preencher opções
        celula_a1 = driver.find_element(By.CSS_SELECTOR, 'input[name="Melhores do ano | Edição do Ano"]')
        celula_a1.click()
        celula_a1.send_keys("#31 Santo Graal")


        celula_a2 = driver.find_element(By.CSS_SELECTOR, 'input[name="Melhores do ano | The Maestro"]')
        celula_a2.click()
        celula_a2.send_keys("#31 Santo Graal")

        # Submeter formulário
        botao_enviar = driver.find_element(By.CSS_SELECTOR, "SELETOR_DO_BOTAO_ENVIAR")
        botao_enviar.click()

        # Aguardar e fechar o navegador
        tempo_espera = random.uniform(40, 120)
        time.sleep(tempo_espera)

# Fechar o navegador apenas uma vez após o término do loop
driver.quit()
