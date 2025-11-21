# 🧪 Automação de Testes com Selenium - Login Lector Live

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-43B02A?style=for-the-badge&logo=selenium)

Este projeto é um estudo de automação de testes web utilizando **Python** e **Selenium WebDriver**. O script executa cenários de teste na página de login do ambiente de homologação da Lector Live.

## 📋 Funcionalidades

O script `main.py` automatiza a validação das seguintes regras de negócio no fluxo de autenticação:

* **Cenário 1:** Tentativa de login com **e-mail inválido**.
    * *Resultado Esperado:* Exibição da mensagem "Usuário ou senha inválidos".
* **Cenário 2:** Tentativa de login com **e-mail correto** e **senha incorreta**.
    * *Resultado Esperado:* Exibição da mensagem "Usuário ou senha inválidos".
* **Cenário 3:** Fluxo de Login com credenciais válidas (Happy Path).

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

* [Python 3.x](https://www.python.org/downloads/)
* [Google Chrome](https://www.google.com/chrome/)
* **Chromedriver**: O executável `chromedriver.exe` já está incluído na raiz deste projeto, mas deve ser compatível com a versão do seu navegador Chrome instalado.

