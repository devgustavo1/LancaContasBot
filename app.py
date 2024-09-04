import openpyxl
import openpyxl.workbook
import pyautogui

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']


for linha in vendas_sheet.iter_rows(min_row=2):
    # nome
    pyautogui.click(311,146,duration=0.5)
    pyautogui.write(linha[0].value)
    # produto
    pyautogui.click(311,175,duration=0.5)
    pyautogui.write(linha[1].value)
    # quantidade
    pyautogui.click(308,208,duration=0.5)
    pyautogui.write(str(linha[2].value))
    # categoria
    pyautogui.click(300,238,duration=0.5)
    pyautogui.write(linha[3].value)
    pyautogui.click(274,277,duration=1.1)
    pyautogui.click(1031,593,duration=1.1)
    
    