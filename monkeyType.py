from selenium import webdriver
import pyautogui
import time
chromedriver = "location of the extracted chromedriver file"
driver = webdriver.Chrome(chromedriver)
driver.get('https://monkeytype.com')
result = driver.find_element_by_id("words")
words = result.get_attribute('innerHTML')

replaceDict = {
    '<div class="word active">':"",
    '<div class="word">':"",
    '<letter>':"",
    '</letter>':"",
    '</div>':" "
}
for word in replaceDict:
    words = words.replace(word, replaceDict[word])
print(words)
time.sleep(5)
#gotta add a timer later
for x in words:
    pyautogui.press(x)
