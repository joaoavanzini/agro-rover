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
 
def Stop():
 init()
 gpio.output(17, False)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, False)
 time.sleep(0.001)
 gpio.cleanup()

 
#sterring controls
print ("Stop")
Stop()
