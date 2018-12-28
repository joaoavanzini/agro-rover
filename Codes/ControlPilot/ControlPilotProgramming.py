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

def Rotation_Right(tf):
 init()
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(tf)
 gpio.cleanup()

def Rotation_Left(tf):
 init()
 gpio.output(23, False)
 gpio.output(24, True)
 time.sleep(tf)
 gpio.cleanup()
 
def Forward(tf):
 init()
 gpio.output(17, True)
 gpio.output(22, False)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(tf)
 gpio.cleanup()
 
def Backward(tf):
 init()
 gpio.output(17, False)
 gpio.output(22, True)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(tf)
 gpio.cleanup()
 
def stop():
 init()
 gpio.output(17, False)
 gpio.output(22, False)
 gpio.output(23, False)
 gpio.output(24, False)
 time.sleep(2)
 gpio.cleanup()

#sterring controls
print("Rotation_Left")
Rotation_Left(1/2)
stop()

print ("Forward")
Forward(1/2)
stop()

print ("Backward")
Backward(1/2)
stop()

print("Rotation_Right")
Rotation_Right(1/2)
stop()