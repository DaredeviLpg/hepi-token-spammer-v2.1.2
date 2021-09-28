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
id = str(input("Guild id\n>")).replace(" ", "")
browser.get("https://discord.com/channels/"+id)

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
        browser.find_element_by_class_name("button-gP4R86.button-38aScr.lookOutlined-3sRXeN.colorWhite-rEQuAQ.grow-q77ONN")
        break
      except:
        pass
    while True:
      try:
        browser.execute_script('document.getElementsByClassName("button-gP4R86 button-38aScr lookOutlined-3sRXeN colorWhite-rEQuAQ grow-q77ONN")[0].click()')
        browser.execute_script('document.getElementsByClassName("inputDefault-3JxKJ2 input-3ITkQf")[0].click();document.getElementsByClassName("submitButton-YEItfy button-38aScr lookFilled-1Gx00P colorGreen-29iAKY sizeMedium-1AC_Sl grow-q77ONN")[0].click();')
        break
      except:
        pass
    print(d[token]["user"]+" has bypassed membership screening.")
    browser.delete_all_cookies()

browser.quit()
