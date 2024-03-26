# Teste de Automação com Selenium em Python

Este é um projeto de automação de testes utilizando Selenium em Python.

## Funcionalidades Implementadas

O projeto possui automação para os seguintes cenários:

1. **Registro de Usuário:** Preenche um formulário de registro com informações personalizadas.
2. **Manipulação de Frames:** Escreve "Olá Mundo" dentro de um frame.
3. **Seleção de Data em Datapicker:** Insere uma data específica em um datapicker.
4. **Movimento de Barra Deslizante:** Move 50% de uma barra deslizante.

## Requisitos

- Python 3.x instalado no sistema.
- Chrome WebDriver instalado e configurado no sistema.

## Configuração

1. Clone este repositório em sua máquina local:
git clone https://github.com/Fellipe-Nunes/teste-python-selenium.git

2. Navegue até a pasta do projeto:
cd nome_do_repositorio

3. Crie um ambiente virtual (opcional, mas recomendado):
python3 -m venv venv

4. Ative o ambiente virtual:
- No Windows:
venv\Scripts\activate

- No Linux/macOS:
source venv/bin/activate

5. Instale as dependências do projeto:
pip install -r requirements.txt

## Execução

Para executar os testes automatizados, siga os seguintes passos:

1. Certifique-se de que o ambiente virtual está ativado (se você optou por criá-lo).
2. Execute o script `automation_test.py` localizado na pasta `src`:

python src/automation_test.py

Isso executará os testes para cada cenário definido no arquivo de configuração correspondente.

## Evidências

As evidências dos testes, como capturas de tela, serão salvas na pasta `screenshots`.
