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
invite = str(input("invite URL\n>")).replace(" ", "")
browser.get(invite)

with open("tokeninfo.json", "r") as f:
  d = json.load(f)

with open("filteredtokens.txt","r") as f:
  tokens = f.read().split(";")[0].split("\n")
  for x in tokens:
    token = x
    script = '''function login(token) { setInterval(() => {  document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"` }, 50);  setTimeout(() => {   location.reload();  }, 2500); }
            login("'''+token+'''")'''
    browser.execute_script(script)
    while True:
      try:
        browser.find_element_by_class_name("title-jXR8lp.marginBottom8-AtZOdT.base-1x0h_U.size24-RIRrxO")
      except:
        break
    while True:
      try:
        browser.find_element_by_class_name("marginTop40-i-78cZ.button-3k0cO7.button-38aScr.lookFilled-1Gx00P.colorBrand-3pXr91.sizeLarge-1vSeWK.fullWidth-1orjjo.grow-q77ONN").click()
        break
      except:
        pass
    while True:
        try:
          browser.find_element_by_class_name("title-jXR8lp.marginBottom8-AtZOdT.base-1x0h_U.size24-RIRrxO")
          break
        except:
          pass
    print(d[token]["user"]+" has joined.")
    browser.delete_all_cookies()

browser.quit()
