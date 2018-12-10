from selenium import webdriver
import webbrowser

#driver = webbrowser.open('https://web.whatsapp.com/')
#'''C:\Users\Fabricio\Desktop\chromedriver'''
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

all_name = ['Teste', 'Mensagem', 'Ana Luyza', 'Bot', 'Sansao']
msg = "Promoção 10% de desconto no queijo"
count = 2

input('Aperte ENTER após ler o QR Code')

for name in all_name:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
