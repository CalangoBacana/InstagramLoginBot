from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagramBot:
	def __init__(self, username, password):
	 self.username = username
	 self.password = password
	 self.driver = webdriver.Chrome(executable_path= COLOQUE AQUI O CAMINHO DO CHROMEDRIVER EX: "C:\\Users\\Luiz\\Documents\\python\\chromedriver.exe") 

	def login(self):
	 driver = self.driver
	 driver.get("https://www.instagram.com")
	 time.sleep(3)
	 campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
	 campo_usuario.click()
	 campo_usuario.clear()
	 campo_usuario.send_keys(self.username)
	 campo_senha = driver.find_element_by_xpath("//input[@name='password']")
	 campo_senha.click()
	 campo_senha.clear()
	 campo_senha.send_keys(self.password)
	 campo_senha.send_keys(Keys.RETURN)
	 
igBot = instagramBot('COLOQUE AQUI SEU NOME DE USUARIO', 'COLOQUE AQUI SUA SENHA')
igBot.login()
