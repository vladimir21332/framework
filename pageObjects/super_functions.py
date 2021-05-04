from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)


########### POP UP ###################

# handle pop-up window (java-script)

driver.get ('https....')
driver.find_element(By.NAME,'...').click()

alert = driver.switch_to.alert #!!!!!!!!!!!
print(alert.text)
alert.accept() # accept it - click on ok
alert.dismiss() # cancel the pop-up
alert.send_keys('...') # sending data to the box

driver.quit()
driver.switch_to.default_content() #!!!!!!!!!!!!!!!!

###################   POP UP AUTHENTICATION ##################
# username = admin
# password = admin
# so you just pass it with driver open url
driver.get('http://admin:admin@ URL')


################# FILE UPLOAD ###############

