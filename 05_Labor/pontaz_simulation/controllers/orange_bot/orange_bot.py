"""orange_bot_full controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard, Motor
from math import pi, sin
robot = Robot()
timestep = int(robot.getBasicTimeStep())
# Keyboard init
keyboard=Keyboard()
keyboard.enable(timestep)
# Sensors init
sensors = []
sensorNames = ['HEAD_distance', 'HEAD_sensor', 'touch1']
for i in range(sensorNames.__len__()):
    sensors.append(robot.getDevice(sensorNames[i]))
    sensors[i].enable(timestep)
# Motors init
motors = []
motorsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4','HEAD_motor']
for i in range(5):
    motors.append(robot.getDevice(motorsNames[i]))
    motors[i].setPosition(float('inf'))
    motors[i].setVelocity(0.0)
# Variables
HeadFrequency = 2
t = 0
avl = 0

# Constants
HEAD_CENTER = 90
NEGATIVE_LOW = 0
NEGATIVE_HIGH = 88
POSITIVE_LOW = 92
POSITIVE_HIGH = 180
DISTANCE_MIN = 0
DISTANCE_MAX = 950



# functions
def radToDeg(rad):
    return rad * 180/pi

def controllERR(head_distance,\
                head_degree,\
                negative_low,\
                negative_high,\
                positive_low,\
                positive_high,\
                distance_min,\
                distance_max):
    pass
    
    
left_speed = 0.0
right_speed = 0.0
# Main loop
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    #leftSpeed = 0.0
    #rightSpeed = 0.0
    key=keyboard.getKey()
    if (key==ord('W')):
        left_speed = 2.0
        right_speed = 2.0
    if (key==ord('S')):
        left_speed = -2.0
        right_speed = -2.0
    if (key==ord('A')):
        left_speed = -2.0
        right_speed = 2.0
    if (key==ord('D')):
        left_speed = 2.0
        right_speed = -2.0
        
    print(sensors[0].getValue())
    print(radToDeg(sensors[1].getValue()))
    
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    
    #motors[0].setVelocity(leftSpeed)
    #motors[1].setVelocity(rightSpeed)
    #motors[2].setVelocity(leftSpeed)
    #motors[3].setVelocity(rightSpeed)
    
    
    position = sin(t * 0.1 * pi * HeadFrequency)
    motors[4].setVelocity(position)
    cur_head_sensor = sensors[0].getValue()
    cur_head_degree = sensors[1].getValue()
    if cur_head_degree > NEGATIVE_LOW and cur_head_degree < NEGATIVE_HIGH and not avl:
        if cur_head_sensor > DISTANCE_MIN and cur_head_sensor < DISTANCE_MAX:
            left_speed = 0.0
            right_speed = -10.0
            #avoid_distance_loop = 100
        else:
            left_speed = 1.0
            right_speed = 1.0
    elif cur_head_degree > POSITIVE_LOW and cur_head_degree < POSITIVE_HIGH and not avl:
        if cur_head_sensor > DISTANCE_MIN and cur_head_sensor < DISTANCE_MAX:
            left_speed = -10.0
            right_speed = 0.0
            #avoid_distance_loop = 100
        else:
            left_speed = 1.0
            right_speed = 1.0
    else:
        if cur_head_sensor > DISTANCE_MIN and cur_head_sensor < DISTANCE_MAX and not avl:
            left_speed = -10.0
            right_speed = -10.0
            #avoid_distance_loop = 100

    motors[0].setVelocity(left_speed)
    motors[1].setVelocity(right_speed)
    motors[2].setVelocity(left_speed)
    motors[3].setVelocity(right_speed)
    print(f'Left Speed: {left_speed}| Right Speed: {right_speed}')

            
        
    t += timestep / 1000.0

    


# Enter here exit cleanup code.

