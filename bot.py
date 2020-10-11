from numpy import *
from PIL import ImageGrab, ImageOps
import pyautogui as py
import time

def salto():
    py.keyDown('space')
    time.sleep(0.3)
    py.keyUp('space')

def calcularArea():
    Box = (730, 200, 850, 222)
    image = ImageGrab.grab(Box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return arr.sum()

def calcularArea2():
    Box = (400, 200, 520, 222)
    image = ImageGrab.grab(Box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return arr.sum()

def run():
    while True:
        a = calcularArea()
        a2 = calcularArea2()
        resultado = abs(a2-a)/a*100

        if resultado < 2:
            pass
        else:
            salto()
   
run()