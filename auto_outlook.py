from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

from curses.ascii import isdigit
import imaplib
import email


import random
import string
letters = string.ascii_letters





def urlGmail():
    chromedriver = Service(ChromeDriverManager().install())
    url = 'https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1663167632&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3da8c32bae-f5ed-f006-8381-e079904683bc&id=292841&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=963b85a999964466bdae6f8f906cb826'
    url2 = 'https://www.instagram.com/accounts/emailsignup/'
    gmail_driver = webdriver.Chrome(service=chromedriver)
    for i in range(1):

            # Step1: Automatically Create Account in Outlook

            gmail_driver.implicitly_wait(1)
            gmail_driver.get(url)
            time.sleep(3)

            inputemail=gmail_driver.find_element(by=By.XPATH, value='//*[@id="MemberName"]')
            inputemail.send_keys('kavirpor')
            time.sleep(3)

            buttonElement=gmail_driver.find_element(by=By.XPATH, value='//*[@id="iSignupAction"]')
            buttonElement.click()
            time.sleep(3)

            inputpassword=gmail_driver.find_element(by=By.XPATH, value='//*[@id="PasswordInput"]')
            inputpassword.send_keys('kavir369')
            time.sleep(3)

            buttonElement=gmail_driver.find_element(by=By.XPATH, value='//*[@id="iSignupAction"]')
            buttonElement.click()
            time.sleep(3)

            inputfirstNname=gmail_driver.find_element(by=By.XPATH, value='//*[@id="FirstName"]')
            inputfirstNname.send_keys('kavir')
            time.sleep(3)

            inputlastName=gmail_driver.find_element(by=By.XPATH, value='//*[@id="LastName"]')
            inputlastName.send_keys('kavirmanesh')
            time.sleep(3)

            buttonElement=gmail_driver.find_element(by=By.XPATH, value='//*[@id="iSignupAction"]')
            buttonElement.click()
            time.sleep(3)

            country=gmail_driver.find_element(by=By.XPATH, value='//*[@id="Country"]')
            country.click()
            time.sleep(3)
            buttonElementNext=gmail_driver.find_element(by=By.XPATH, value='//*[@id="Country"]/option[106]')
            buttonElementNext.click()
            time.sleep(3)
            
            month=gmail_driver.find_element(by=By.XPATH, value='//*[@id="BirthMonth"]')
            month.click()
            time.sleep(3)
            buttonElementNext=gmail_driver.find_element(by=By.XPATH, value='//*[@id="BirthMonth"]/option[8]')
            buttonElementNext.click()
            time.sleep(3)

            day=gmail_driver.find_element(by=By.XPATH, value='//*[@id="BirthDay"]')
            day.click()
            time.sleep(3)
            buttonElementNext=gmail_driver.find_element(by=By.XPATH, value='//*[@id="BirthDay"]/option[14]')
            buttonElementNext.click()
            time.sleep(3)

            yar=gmail_driver.find_element(by=By.XPATH, value='//*[@id="BirthYear"]')
            yar.send_keys('1989')
            time.sleep(5)

            buttonElement=gmail_driver.find_element(by=By.XPATH, value='//*[@id="iSignupAction"]')
            buttonElement.click()
            time.sleep(30)
            
            buttonElement=gmail_driver.find_element(by=By.XPATH, value='/html/body/div[5]/span/a[2]')
            buttonElement.click()
            time.sleep(5)

            # Step2: Activate imap in Outlook

            

#####################################################################################################
            # Step3: Automatically Create Account in Instagram

            gmail_driver.implicitly_wait(1)
            gmail_driver.get(url2)
            time.sleep(7)

            inputemail=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input')
            inputemail.send_keys('khoshvakhoram@outlook.com')
            time.sleep(3)

            x = "".join(random.sample(letters,5))
            inputfullname=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[2]/div/label/input')
            inputfullname.send_keys(x)
            time.sleep(3)

            x2 = "".join(random.sample(letters,5))
            inputusername=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input')
            inputusername.send_keys(x2+'sthsfrjhfr')
            time.sleep(3)

            x3 = "".join(random.sample(letters,5))
            inputpassword=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input')
            inputpassword.send_keys(x3+'123')
            time.sleep(3)
            print(x3+'123')

            buttonElement=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[5]/div')
            buttonElement.click()
            time.sleep(3)

            month=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select')
            month.click()
            time.sleep(3)
            buttonElementNext=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[11]')
            buttonElementNext.click()
            time.sleep(3)

            day=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select')
            day.click()
            time.sleep(3)
            buttonElementNext=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[4]')
            buttonElementNext.click()
            time.sleep(3)

            year=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
            year.click()
            time.sleep(3)
            buttonElementNext=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[22]')
            buttonElementNext.click()
            time.sleep(3)

            buttonElement=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
            buttonElement.click()
            time.sleep(3)




            # Step4: Featch Verification Code of Email That Created in Step1

            key = 'FROM'  
            value = 'no-reply@mail.instagram.com'
            user = "khoshvakhoram@outlook.com"
            password = "147258369khosh"

            my_mail = imaplib.IMAP4_SSL('outlook.office365.com')
            my_mail.login(user,password)
            my_mail.select('Inbox')

                
            _, data = my_mail.search(None, key, value)  #Search for emails with specific key and value
            mail_id_list = data[0].split()  #IDs of all emails that we want to fetch 
            msgs = [] # empty list to capture all messages


            for num in mail_id_list:
                typ, data = my_mail.fetch(num, '(RFC822)') #RFC822 returns whole message (BODY fetches just body)
                msgs.append(data)
            # print(msgs)
            # msgs.reverse()
                    

            num0=1;
            AllSubjects=[];
            for msg in msgs[::-1]:
                for response_part in msg:
                    if type(response_part) is tuple:
                        my_msg=email.message_from_bytes((response_part[1]))
                        AllSubjects=my_msg['subject']
                        AllSubjects=str(AllSubjects)
                        InsNum=AllSubjects[0:6];
                        if isdigit(InsNum[1]):
                            print(InsNum)
                            FetchedCode=InsNum
                            break
                    break
                break




            code=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')
            code.send_keys(FetchedCode)
            time.sleep(3)

            buttonElement=gmail_driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
            buttonElement.click()
            time.sleep(30)

urlGmail()