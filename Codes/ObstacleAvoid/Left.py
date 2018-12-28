#/-------------------------------------------\
#|-----------robotecweb.com.br---------------|
#|-TODOS OS DIREITOS RESERVADOS PARA ROBOTEC-|
#|------ALL RIGHTS RESERVED TO ROBOTEC-------|
#|-----------COPYRIGHT TO ROBOTEC------------|
#|-------------------------------------------|
#|---------------AgroRover-------------------|
#|------João Victor Palhares Barbosa---------|
#|------------Mario Avancini-----------------|
#\-------------------------------------------/


#lib from l298n
import RPi.GPIO as gpio
import time


#programming the pins corresponding to the movements
def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(22, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)
 
def Rotation_Left(tf):
 init()
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(tf)
 gpio.cleanup()
 
 
#sterring controls
print("Rotation_Left")
Rotation_Left(1)