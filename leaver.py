import os
try:
  from selenium import webdriver
  from selenium.webdriver.firefox.options import Options
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.common.by import By
except:
  os.system("pip install selenium")
  from selenium import webdriver
  from selenium.webdriver.firefox.options import Options
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.common.by import By
import json


options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
id = input("guild id\n>")

with open("tokeninfo.json", "r") as f:
  d = json.load(f)

with open("filteredtokens.txt","r") as f:
  tokens = f.read().split(";")[0].split("\n")
  for x in tokens:
    browser.get("https://discord.com/channels/"+id)
    token = x
    script = '''function login(token) { setInterval(() => {  document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"` }, 50);  setTimeout(() => {   location.reload();  }, 2500); }
            login("'''+token+'''")'''
    browser.execute_script(script)
    while True:
      try:
        browser.find_element_by_class_name("headerButton-3in1-b")
        break
      except:
        pass
    while True:
      try:
        browser.execute_script('var div = document.getElementsByClassName("headerButton-3in1-b")[0];div.click()')
        break
      except:
        pass
    while True:
        try:
          browser.execute_script('var div = document.getElementsByClassName("label-22pbtT")[6];div.click()')
          break
        except:
          pass
    while True:
      try:
        browser.execute_script('var btn = document.getElementsByClassName("button-38aScr lookFilled-1Gx00P colorRed-1TFJan sizeMedium-1AC_Sl grow-q77ONN")[0];btn.click()')
        break
      except:
        pass
    print(d[token]["user"]+" has left.")
    browser.delete_all_cookies()

browser.quit()
