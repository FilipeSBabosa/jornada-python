# Passo a passo do projeto
# passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time

# cliccar » pyautogui.click
# escrever » pyautogui.write
# apertar  uma tecla » pyautogui.press
# apertar » pyautogui.hotkey
# scroll » pyautogui.scroll

pyautogui.PAUSE = 0.3

# aperta a tecla do windows (comand + barra de espaço)
pyautogui.press("win")
# digite o nome do programa (chrome)
pyautogui.write("chrome")
# apertar enter
pyautogui.press("enter")
# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar enter
pyautogui.press("enter")
# esperar 5 segudos
time.sleep(1)

# passo 2: Fazer login
pyautogui.press("tab")
# pyautogui.click(x=574, y=375)
# escrever o seu email
pyautogui.write("lipebarbosa@gmail.com")
# passar para o campo de senha
pyautogui.press("tab")
# digitar a senha
pyautogui.write("minha senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# passo 3: Importar a base de dados 
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # passo 4: Cadastrar um produto   
    pyautogui.click(x=900, y=238)
    pyautogui.click(x=900, y=238)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab") 
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# passo 5: Repetir isso ate acabar a base de dados
