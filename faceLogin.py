from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass

usr = input('Entre com seu nome de usuário: ')
pwd = getpass('Coloque sua senha: ')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_2')
login_btn.submit()

