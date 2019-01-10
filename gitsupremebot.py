from selenium import webdriver
import time 

driver = webdriver.Chrome(executable_path=#path to chrome driver#)

tim = time.start()

driver.get(#url#)

xpath = '//*[@id="add-remove-buttons"]/input'
add = driver.find_element_by_xpath(xpath)
add.click()

check = '//*[@id="cart"]/a[2]'
checkout = driver.find_element_by_xpath(check)
checkout.click()

name = '//*[@id="order_billing_name"]'
name1 = driver.find_element_by_xpath(name)
name1.send_keys(#name)

email = '//*[@id="order_email"]'
email1 = driver.find_element_by_xpath(email)
email1.send_keys(#email)

tel = '//*[@id="order_tel"]'
telli = driver.find_element_by_xpath(tel)
telli.send_keys(#phone number)

addi = '//*[@id="bo"]'
addi1 = driver.find_element_by_xpath(addi)
addi1.send_keys(#address)

zipc = '//*[@id="order_billing_zip"]'
zipcode = driver.find_element_by_xpath(zipc)
zipcode.send_keys(#add zip)

city = '//*[@id="order_billing_city"]'
city1 = driver.find_element_by_xpath(city)
city1.send_keys(#add city)

#might need new xpath for your state
sta = '//*[@id="order_billing_state"]/option[5]'
state = driver.find_element_by_xpath(sta)
state.click()

number = '//*[@id="nnaerb"]'
numb = driver.find_element_by_xpath(number)
numb.send_keys(#card)

cvv = '//*[@id="orcer"]'
yo = driver.find_element_by_xpath(cvv)
yo.send_keys(#cvv)

proc = '//*[@id="pay"]/input'
procc = driver.find_element_by_xpath(proc)
procc.click()

tim = time.end()

print(tim)

#after you run you still need to solve the captcha 