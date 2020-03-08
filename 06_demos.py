#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:55:00 2020

@author: jose
"""
#%%
# DEMO WEBBOT
# Documentación webbot: 
# https://webbot.readthedocs.io/en/latest/webbot.html
from webbot import Browser
from pprint import pprint
web = Browser(showWindow=True)
web.go_to('https://stackoverflow.com/')
inputs = web.find_elements(tag='input')
inputs[0].send_keys('python')
web.press(web.Key.ENTER)
questions = web.find_elements(id='questions')[0]
links = questions.find_elements_by_class_name("question-hyperlink")
pprint([(link.text, link.get_attribute('href')) for link in links])

#%%
# DEMO WEBBOT LOGIN ON PAGE
password = None
with open('/home/jose/.pass') as my_file:
    password = my_file.read()
user = 'test_mail_client'

web = Browser(showWindow=True)
web.go_to('https://protonmail.com/')
login_button = web.find_elements(text="LOG IN")
login_button[0].click()
elements = web.find_elements(id='username')
elements[0].send_keys(user)

elements = web.find_elements(id='password')
elements[0].send_keys(password)

web.press(web.Key.ENTER)


#%%
# Demo PyAutogui
# Documentación npyautogui
# https://pyautogui.readthedocs.io/en/latest/install.html
import pyautogui
import time
button_location = pyautogui.locateOnScreen('/home/jose/Imágenes/pyautogui/archivo.png')
center = pyautogui.center(button_location)
pyautogui.click(center)
time.sleep(2)
pyautogui.moveRel(None, 160)
time.sleep(2)
pyautogui.click()
time.sleep(2)
pyautogui.write("test")
#%%
# Demo PyAutogui
import pyautogui
pyautogui.click('/home/jose/Imágenes/pyautogui/restaurar.png')

#%%
# Mezclando ambos
from webbot import Browser
import pyautogui
import time

web = Browser()
web.go_to('https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php')
time.sleep(3)
pyautogui.click('/home/jose/Imágenes/pyautogui/captcha.png')

#%%
# FLASK 
# Super fast websites
# https://www.fullstackpython.com/flask.html
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola!'

@app.route('/login')
def login():
    return """
        <html>
            <form method="POST" action="/user">
                <input name="user" />
                <input name="pass" type="password"/>
                <input type="submit" value="login"/>
            </form>
        </html>"""

@app.route('/user', methods=['POST'])
def user():
    if request.form['user'] == 'josete' and request.form['pass'] == 'contraseña':
        return "login correct"
    else:
        return "Permission forbidden"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f"Hola {username}!"

app.run()

#%%
# OCR
# pip install Pillow
# pip install tesseract

import pytesseract
from PIL import Image

img = Image.open("/home/jose/Imágenes/pyautogui/resume.png")
text=pytesseract.image_to_string(img)

print(text)


#%%
# OCR
import os
import pytesseract
from PIL import Image

path ="/home/jose/Imágenes/pyautogui/"
for filename in os.listdir(path):
    if "png" in filename:
        img = Image.open(path + filename)
        text = pytesseract.image_to_string(img)
        if text:
            print(text)
            print("================================")
