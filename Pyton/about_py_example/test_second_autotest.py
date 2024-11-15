#import pytest
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()
#driver.get('https://erikdark.github.io/Qa_autotest_15/')

#def test_push_the_button_and_valid_text():
#    push_the_button = False
#    try:
#        if WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'verify'))).click():
#            push_the_button = True    
#            assert push_the_button == True,'кнопка нажата'         
#        else: 
#            assert push_the_button == False,'кнопка неактивна'   

#        WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.ID,'verify_message')))
#        assert driver.find_element(By.ID,'verify_message').text == 'Verification successful!','текст должен быть Verification successful!'
       
#    finally:
#        time.sleep(3)
#        driver.quit()

#if __name__ == "__main__":
#    import pytest
#    pytest.main()



