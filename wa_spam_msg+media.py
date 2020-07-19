#Author: Swaraj Khan
#DO NOT USE THE CODE IN ANY UNETHICAL PURPOSE

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
print("This is a Code by Swaraj \n to send lots of messages and media files to any contact or group.")
msgtype = input("Which type of message you want to send? 1.Text 2.Media: Select 1 or 2 :")

def txtmsg():
    name = input("Enter name or group name:")
    msg = input("Enter message:")
    count = int(input("Enter count:"))

    input("Enter anything after scanning QR code:")

    user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
    user.click()

    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

    print("Success \n © Swaraj")



def mmsmsg():
    name = input('Enter the name of user or group : ')
    filepath = input('Enter your filepath (images/video): ')
    count = int(input("Enter count:"))

    input('© Swaraj \n Enter anything after scanning QR code:')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    for index in range(count):
        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()
        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filepath)
        sleep(4)
        send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()

    print("Success \n © Swaraj")

if msgtype=="1":
    txtmsg()
elif msgtype=="2":
    mmsmsg()
else:
    print("Wrong Input.")
