# LancaContasBot

O **LancaContasBot** é um bot de automação projetado para facilitar o lançamento contábil de dados. Ele permite que os usuários insiram dados de um arquivo Excel em um sistema específico usando automação de interface gráfica.

## Funcionalidades

- **Leitura de Dados**: O bot lê dados de um arquivo Excel (.xlsx) com informações de clientes, produtos, quantidades e categorias.
- **Automação de Entrada de Dados**: Utiliza a biblioteca `pyautogui` para automatizar a inserção de dados em uma interface gráfica.
- **Interface Gráfica**: Oferece uma interface gráfica para inserir dados manualmente e salvá-los em um arquivo de texto.

## Instalação

1. **Clone o Repositório**:
   git clone https://github.com/devgustavo1/LancaContasBot.git

2. **Navegue para o Diretório do Projeto:**
cd LancaContasBot
3. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado):**
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
4. **Instale as dependências:**
pip install openpyxl pyautogui
## Uso
Prepare o Arquivo Excel:
Crie um arquivo chamado vendas_de_produtos.xlsx com uma planilha chamada vendas.
A planilha deve conter as colunas: Cliente, Produto, Quantidade e Categoria.
## Execute o Script:
Execute o script app.py para iniciar o bot:
python app.py
## Use a Interface Gráfica:
Preencha os campos na interface gráfica.
Clique no botão "Salvar" para salvar os dados em um arquivo de texto.