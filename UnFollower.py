from selenium.webdriver.common.keys import Keys

from time import sleep
import selenium
import random
Drive = selenium.webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#Drive = selenium.webdriver.Firefox()

class Insta():
    def LogIn(UserName,Password):
        Drive.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        InputElements=Drive.find_elements_by_class_name("zyHYP")
        UsernameInput=InputElements[0]
        PasswordInput=InputElements[1]
        UsernameInput.send_keys(str(UserName))
        PasswordInput.send_keys(str(Password))
        Click=Drive.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
        Click.click()
        sleep(10)
    
    def GotoFollowings():
        Drive.get("https://www.instagram.com/urge_ir/")
        sleep(5)
        FollowingsElement=(Drive.find_elements_by_class_name("Y8-fY"))[2]
        FollowingsElement.click()
        sleep(10)
    def ScrollDownFollowings():
        Drive.find_element_by_class_name("HYpXt").click()
        body = Drive.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)
    def UnFollowFollowings(HowMany,RandomMin,RandomMax):
        for i in range (int(HowMany)):
            sleep(1)
            List=Drive.find_elements_by_class_name("_8A5w5")
            List=List[1:len(List)]
            print ("i=",i)
            print ("len =",len(List))
            while len(List)<2:
                Insta.ScrollDownFollowings()
                List=Drive.find_elements_by_class_name("_8A5w5")
                List=List[1:len(List)]
                sleep(2)
                
            List[0].click()
            sleep(3)
            Drive.find_element_by_class_name("-Cab_").click()
            sleep(random.uniform(RandomMin, RandomMax)) 
while True:            
    Insta.LogIn(UserName,Password)
    Insta.GotoFollowings()
    Insta.UnFollowFollowings(50,1,10)