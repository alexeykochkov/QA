
#import time
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()
#driver.get('https://erikdark.github.io/Qa_autotests_17/')

#def test_by_all_car():
#    try:
#        first = False
#        second = False
#        third = False
#        all_true = False
        
#        if WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.ID,'price1'),'550')):
#            driver.find_element(By.ID,'buyButton1').click()
#            first = True
#        if WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.ID,'price2'),'800')):
#            driver.find_element(By.ID,'buyButton2').click()
#            second = True
#        if WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.ID,'price3'),'19000')):
#            driver.find_element(By.ID,'buyButton2').click()
#            third = True
#        if first == True and second == True and third == True:
#            assert all_true == True,'Все куплено'
#        else:
#            assert all_true == False,'Не получилось'

 #   finally:
 #       time.sleep(3)
 #       driver.quit()




