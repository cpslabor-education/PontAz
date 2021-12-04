# Ev3DeV Self driving robot
# Last update 2021.11.19 by CCCompiler

# Import Ev3dev packages
#from keyboard import on_press


from ev3dev2.motor import LargeMotor,\
                          MediumMotor,\
                          SpeedPercent,\
                          MoveTank,\
                          OUTPUT_A,\
                          OUTPUT_B,\
                          OUTPUT_C

from ev3dev2.sensor.lego import ColorSensor,\
                                LightSensor,\
                                TouchSensor,\
                                UltrasonicSensor,\
                                InfraredSensor

from ev3dev2.button import Button

from ev3dev2.led import Leds

from ev3dev2.sound import Sound

# Import other packages
import time
import math
import threading
#import keyboard

# Setup
IR_SENSOR = False

# Varianles and constants
headMotor = None
leftDriveMotor = None
rightDriveMotor = None

headMotor = MediumMotor(OUTPUT_C)
leftDriveMotor = LargeMotor(OUTPUT_B)
rightDriveMotor = LargeMotor(OUTPUT_A)

speak = Sound()

headSensor = None
"""
if IR_SENSOR:
    headSensor = InfraredSensor()
    pass
else:
"""
headSensor = UltrasonicSensor()

leds = Leds()

driving_value = 0
driving_position = 0
current_proximity = 0

# Calculate direction
def calculate_dir(neg_low_bound,\
                  neg_high_bound,\
                  dist_low,\
                  dist_high,\
                  pos_low_bound,\
                  pos_high_bound,\
                  current_distance,\
                  current_position):
    low_val = 1 if current_position < neg_low_bound and current_position > neg_high_bound else 0
    high_val = 1 if current_position > pos_low_bound and current_position < pos_high_bound else 0
    dist_val = 1 if current_distance > dist_low and current_distance < dist_high else 0
    return ((1 if dist_val and low_val else 0)-(1 if dist_val and high_val else 0))

running = True
# Driving Thread
def driving(value):

    leftDriveMotor.stop_action = "coast"
    rightDriveMotor.stop_action = "coast"
    

    while running:
        print(value, "Driving...")
        if driving_value == 0:
            leftDriveMotor.on(SpeedPercent(-20), brake=False, block=False)
            rightDriveMotor.on(SpeedPercent(-20), brake=False, block=False)
        elif driving_value == 1:
            rightDriveMotor.on(SpeedPercent(50), brake=False, block=False) # -50 false false
            leftDriveMotor.on(SpeedPercent(driving_position), brake=False, block=False)
            if current_proximity < 25:
                speed = ((current_proximity-30)-(2*(current_proximity-30)))
                leftDriveMotor.on(SpeedPercent(speed), brake=False, block=False)
                rightDriveMotor.on(SpeedPercent(speed), brake=False, block=False)
        elif driving_value == -1:
            leftDriveMotor.on(SpeedPercent(50), brake=False, block=False)
            rightDriveMotor.on(SpeedPercent(driving_position), brake=False, block=False)
            if current_proximity < 25:
                speed = ((current_proximity-30)-(2*(current_proximity-30)))
                leftDriveMotor.on(SpeedPercent(speed), brake=False, block=False)
                rightDriveMotor.on(SpeedPercent(speed), brake=False, block=False)
        
        time.sleep(0.01)

t1 = threading.Thread(target=driving, args=(1,))

# Main function
def main():
    # Define local variables
    print('Initializing...')
    speak.speak('Indulás')
    leds.set_color("LEFT", "ORANGE")
    leds.set_color("RIGHT", "ORANGE")
    global driving_value
    global driving_position
    global current_proximity
    head_next_pos_res = 20 # default: 20
    head_next_pos_val = 100
    head_next_pos = []
    for _ in range(int(head_next_pos_val/head_next_pos_res)):
        head_next_pos.append(int(head_next_pos_res))
    for _ in range(int(2*(head_next_pos_val/head_next_pos_res))):
        head_next_pos.append(int(-head_next_pos_res))
    for _ in range(int(head_next_pos_val/head_next_pos_res)):
        head_next_pos.append(int(head_next_pos_res))
    head_next_pos_total = 4*(head_next_pos_val/head_next_pos_res)

    loop = 0

    headMotor.stop_action = "coast"
    headMotor.speed_sp = 20
    


    time.sleep(1)
    leds.set_color("LEFT", "GREEN")
    leds.set_color("RIGHT", "GREEN")
    print('Starting Loop...')
    speak.speak('Igen')
    t1.daemon = True
    t1.start()
    # Loop start
    while True: #not TouchSensor().is_pressed:
        loop = 0 if loop == head_next_pos_total else loop
        print("loop: ", loop,\
              "head_next_pos: ", head_next_pos[loop],\
              "headMotor.position: ", headMotor.position)
        #headMotor.position_sp = head_next_pos[loop]
        # Rotate the head motor
        power = 3 if current_proximity < 25 else 20
        headMotor.on_for_degrees(SpeedPercent(power),\
            head_next_pos[loop],\
            brake=False,\
            block=False
        )

        # Read the head sensor
        current_proximity = headSensor.distance_centimeters

        driving_position = headMotor.position

        print("headSensor: ", current_proximity, "headPosition: ", driving_position)

        driving_value = calculate_dir(-1, -100, 0, 25, 1, 100, current_proximity, driving_position)
        
        print("driving_value: ", driving_value, "driving_pos: ", driving_position, "cur_prox: ", current_proximity)

        loop += 1
        speak.speak('A')
        time.sleep(0.01)
    
#    keys = None

#    while not TouchSensor().is_pressed:
#        if keyboard.is_pressed('w'):
#            leftDriveMotor.on(SpeedPercent(20), brake=False, block=False)
#            rightDriveMotor.on(SpeedPercent(20), brake=False, block=False)
#        elif keyboard.is_pressed('s'):
#            leftDriveMotor.off()
#            rightDriveMotor.off()
#    clear()
#    exit()
    


def clear():
    global running
    leds.set_color("LEFT", "RED")
    leds.set_color("RIGHT", "RED")
    headMotor.position_sp = 0
    headMotor.speed_sp = 20
    headMotor.stop_action = 'hold'
    headMotor.run_to_abs_pos()
    time.sleep(1)
    
    running = False
    time.sleep(1)
    leftDriveMotor.off()
    rightDriveMotor.off()
    leds.set_color("LEFT", "GREEN")
    leds.set_color("RIGHT", "GREEN")
    pass

# Safe start
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        exit()