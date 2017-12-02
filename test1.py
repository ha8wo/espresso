import pygame
from pygame.locals import *
import os
from time import sleep
import RPi.GPIO as GPIO

#Setup the GPIOs as outputs - only 4 and 17 are available
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

#Colours
WHITE = (255,255,255)

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(True)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,100,100))
pygame.display.update()

font_big = pygame.font.Font(None, 50)

touch_buttons = {'17 on':(80,60), '4 ON':(240,60), '17 OFF':(80,180), '4 off':(240,180)}

for k,v in touch_buttons.items():
    text_surface = font_big.render('%s'%k, True, WHITE)
    rect = text_surface.get_rect(center=v)
    lcd.blit(text_surface, rect)

pygame.display.update()

while True:
    if pygame.event.get():
        true
    
    sleep(0.1)
