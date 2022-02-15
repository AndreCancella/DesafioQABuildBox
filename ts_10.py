from ast import Break
import tkinter
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from tkinter import messagebox
import sys

browser = webdriver.Chrome()
browser.get('https://buger-eats.vercel.app')
browser.maximize_window()
time.sleep(5)

#Botão
btnCadastrar= browser.find_element_by_xpath('/html/body/div/div/div/main/a')
btnCadastrar.click()
time.sleep(5)

#Dados
lblNome = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[1]/div[1]/div[1]/input')
lblNome.send_keys('André Cancella')
time.sleep(4)
lblCPF = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[1]/div[1]/div[2]/input')
lblCPF.send_keys('09245582664')
time.sleep(4)
lblEmail = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[1]/div[2]/div[1]/input')
lblEmail.send_keys('abc@gmail.com')
time.sleep(4)
lblWhats = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[1]/div[2]/div[2]/input')
lblWhats.send_keys('38999306639')
time.sleep(5)

#Endereço
lblCEP = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[2]/div[1]/div[1]/input')
lblCEP.send_keys('38654000')
time.sleep(5)
btnBuscar = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[2]/div[1]/div[2]/input')
btnBuscar.click()
time.sleep(5)

lblRua = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[2]/div[2]/input')
if lblRua.is_enabled():
        lblRua.send_keys('Josias Barbosa Ribeiro')
        time.sleep(5)
else:
    messagebox.showinfo("ERRO", "Campo não habilitado")
    sys.exit()

lblNum = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[2]/div[3]/div[1]/input')
lblNum.send_keys('251')
time.sleep(5)
#lblBairro = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[2]/div[4]/div[1]/input')
#lblBairro.send_keys('Alto boa vista')
#time.sleep(5)

#Metodo de entrega
btnMoto = browser.find_element_by_xpath('/html/body/div/div/form/fieldset[3]/ul/li[1]')
btnMoto.click()
time.sleep(5)

#Cadastrar
btnCadstro = browser.find_element_by_xpath('/html/body/div/div/form/button')
btnCadstro.click()
time.sleep(8)