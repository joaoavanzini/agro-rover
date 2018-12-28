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


#lib from HCSR04 
import os
import sys
import time
import signal
import RPi.GPIO as GPIO


#defintations of pins
GPIO.setmode(GPIO.BOARD)

#finalize program with security mode (CRTL-C)
def sigint_handler(signum, instant):
    GPIO.cleanup()
    sys.exit()

#capture of sinal SIGINT (Ctrl-C)
signal.signal(signal.SIGINT, sigint_handler)

#TRIG and ECHO connections
TRIG = 13
ECHO = 12

#aid variables
sampling_rate = 20.0
speed_of_sound = 349.10
max_distance = 4.0
max_delta_t = max_distance / speed_of_sound
start_t = 0
end_t = 0

#sets TRIG as digital output
#sets ECHO as digital input
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#initializes TRIG at low logic level
GPIO.output(TRIG, False)
time.sleep(1)


#loop (CRTL-C)
while True:

    #created waves
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    #waves send
    while GPIO.input(ECHO) == 0:
      start_t = time.time()

    #waves reflected - waiting for this moment  
    while GPIO.input(ECHO) == 1 and time.time() - start_t < max_delta_t:
      end_t = time.time()

    #calc distance based in waves  
    if end_t - start_t < max_delta_t:
        delta_t = end_t - start_t
        distance = 100*(0.5 * delta_t * speed_of_sound)
    else:
        distance = -1

    #show the distance arredonding with 2 houses
    print (round(distance, 2))

    #delay slow
    time.sleep(1/sampling_rate)

    #direction of car 
    if (round(distance, 2)) >= 20:
        os.system('python3 Forward.py')
    else:   
        os.system('python3 Backward.py')
        os.system('python3 Left.py')
        time.sleep(0.000001)
        leftvar = (round(distance, 2)) 
        os.system('python3 Stop.py')
        os.system('python3 Right.py')
        os.system('python3 Right.py')
        time.sleep(0.000001)
        os.system('python3 Left.py')
        rightvar = (round(distance, 2)) 

        if leftvar > rightvar:
            os.system('python3 Left.py')
            os.system('python3 Forward.py')
        else:
            os.system('python3 Right.py')
            os.system('python3 Forward.py')    