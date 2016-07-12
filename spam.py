from selenium import webdriver
b = webdriver.Chrome('<Path to your chrome webdriver>')
b.get('https://web.whatsapp.com')
raw_input()
elem = b.find_element_by_xpath('//span[contains(text(),"<Your friend name>")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
while True:
     elem1[1].send_keys('<Your spam messege>')
     b.find_element_by_class_name('send-container').click()
