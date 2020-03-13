from selenium import webdriver
from time import sleep

# secretaksis kullanıcı adı ve şifre içermeli
from secretaksis import kullanici,sifre

class aksisBot(object):
    """docstring for aksisBot."""

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://aksis.istanbulc.edu.tr/')
        sleep(3)

        kullanici_in = self.driver.find_element_by_xpath('//*[@id="UserName"]')
        kullanici_in.send_keys(kullanici)

        sifre_in = self.driver.find_element_by_xpath('//*[@id="Password"]')
        sifre_in.send_keys(sifre)

        sleep(1)

        girisButon = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        girisButon.click()

        sleep(1)

        obs = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div[2]/div[1]')
        obs.click()

        self.driver.switch_to_window(self.driver.window_handles[1])

        sleep(1)
        ogrBilgi = self.driver.find_element_by_xpath('//*[@id="sidebar"]/li[10]/a')
        ogrBilgi.click()

        sleep(1)
        sinavSonucButon = self.driver.find_element_by_xpath('//*[@id="sidebar"]/li[10]/ul/li[2]')
        sinavSonucButon.click()

        sleep(1)
        sinavSonuc = self.driver.find_element_by_xpath('//*[@id="sinavSonucGrid"]/table/tbody/tr[29]/td[7]')
        self.driver.execute_script("arguments[0].innerText = '200'", sinavSonuc)

        self.driver.get('https://web.whatsapp.com/')
        sleep(15)

        self.driver.switch_to_window(self.driver.window_handles[1])

        btn = self.driver.find_element_by_xpath('//*[@title="Ben"]')
        btn.click()

        yaziyeri = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        yaziyeri.send_keys("ALGORITMADAN AA ALDIN")

        tikla = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
        tikla.click()




bot = aksisBot()
bot.login()
