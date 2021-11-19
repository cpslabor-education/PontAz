# 04_Automatic_And_Intelligent_Robots course
#
# robot node: 
# 
# Simulate a robot that has 2 driver motor (A, B) and a head with an ultrasonic sensor
# and a motor (C)
# The node returns a string with the motor's speed/deg and the ultrasonic's 
# sensor raw/real values
#
# | Topic     | Variable      | Value at program start | Range                 |
# | --------- |-------------- | ---------------------- | --------------------- |
# | topic_01: | AMotorSpeed   | 0                      | -100 - 100            |
# | topic_02: | AMotorDeg     | 0                      | -infinity - infinity  |
# | topic_03: | BMotorSpeed   | 0                      | -100 - 100            |
# | topic_04: | BMotorDeg     | 0                      | -infinity - infinity  |
# | topic_05: | CMotorSpeed   | 0                      | -100 - 100            |
# | topic_06: | CMotorDeg     | 0                      | -infinity - infinity  |
# | topic_07: | UltrasonicRaw | 0                      | 0 - 4096              |
# | topic_08: | TouchSensor   | 0                      | bool                  |
# | topic_09: | RGBSensor     | tuple(0, 0, 0)         | 0 -4096               |
# | topic_99: | ............. | ...................... | 999999999 - 999999999 |
#
#
#
# Created by: Füleki Tamás 2021.10.20

from numpy.core.records import array
import rclpy
from rclpy.node import Node

import random
from std_msgs.msg import String,\
                         Float64,\
                         Bool,\
                         Int32MultiArray,\
                         Int64,\
                         Int32,\
                         Float64MultiArray

import numpy as np
import random

import sys

#from pontaz.msg import Num

def genSin(res, j=1):
    x = np.linspace(-np.pi, np.pi, res)
    y = np.sin(x*j)
    return (x, y)

def getRandInRange(min, step, max):
    return random.randrange(start=min, step=step, stop=max)

def myMap(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

class Robot(Node):
 
    def __init__(self):
        super().__init__('robot')
        # initialize topics
        self.topic_01 = self.create_publisher(Float64, 'amotorspeed', 10)
        self.topic_02 = self.create_publisher(Float64, 'amotordeg', 10)
        self.topic_03 = self.create_publisher(Float64, 'bmotorspeed', 10)
        self.topic_04 = self.create_publisher(Float64, 'bmotordeg', 10)
        self.topic_05 = self.create_publisher(Float64, 'cmotorspeed', 10)
        self.topic_06 = self.create_publisher(Float64, 'cmotordeg', 10)
        self.topic_07 = self.create_publisher(Int32, 'ultrasonicraw', 10)
        self.topic_08 = self.create_publisher(Bool, 'touchsensor', 10)
        self.topic_09 = self.create_publisher(Int32, 'rgbsensor_r', 10)
        self.topic_10 = self.create_publisher(Int32, 'rgbsensor_g', 10)
        self.topic_11 = self.create_publisher(Int32, 'rgbsensor_b', 10)

        # self.publisher_ul = self.create_publisher(Float64, 'ul', 10)
        # timer sends packets in every 0.5 seconds
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        

    def timer_callback(self):
        # Messages types 
        msg_amotorspeed = Float64()
        msg_amotordeg = Float64()
        msg_bmotorspeed = Float64()
        msg_bmotordeg = Float64()
        msg_cmotorspeed = Float64()
        msg_cmotordeg = Float64()

        msg_ultrasonicraw = Int32()

        msg_touchsensor = Bool()

        msg_rgbsensor_r = Int32()
        msg_rgbsensor_g = Int32()
        msg_rgbsensor_b = Int32()
        
        #msg.data = 'Hello World: %d' % self.i
        #msg.data = self.robot.msgData()+str(self.i)
        # Get sensors data
        msg_amotorspeed.data = float(random.randrange(start=-100, stop=100, step=1))
        msg_amotordeg.data = float(random.randrange(start=0, stop=360, step=1))
        msg_bmotorspeed.data = float(random.randrange(start=-100, stop=100, step=1))
        msg_bmotordeg.data = float(random.randrange(start=0, stop=360, step=1))
        msg_cmotorspeed.data = float(random.randrange(start=-100, stop=100, step=1))
        msg_cmotordeg.data = float(random.randrange(start=-180, stop=180, step=1))
        #msg_cmotorspeed.data = float(random.randrange(
        #    start=int(myMap(abs(int(genSin(100, 2)[0][
        #        self.i if self.i < 100 else int(myMap(self.i, 0, self.i, 0, 100))
        #    ]*4096)), 0, 5000, 0, 4096)), stop=4096)
        #)
        #msg_cmotordeg.data = float(random.randrange(
        #    start=abs(int(genSin(100, 2)[1][
        #        self.i if self.i < 100 else int(myMap(self.i, 0, self.i, 0, 100))
        #    ]*4096)), stop=4096)
        #)
        msg_ultrasonicraw.data = random.randrange(start=0, stop=4096, step=1)
        msg_touchsensor.data = bool(random.getrandbits(1))
        #r = int(random.randrange(0, 4096, 1))
        #g = int(random.randrange(0, 4096, 1))
        #b = int(random.randrange(0, 4096, 1))
        #r = 4096
        #g = 4096
        #b = 4096

        #msg_rgbsensor.data = (r<<24|g<<12|b)
        msg_rgbsensor_r.data = random.randrange(start=0, stop=4096, step=1)
        msg_rgbsensor_g.data = random.randrange(start=0, stop=4096, step=1)
        msg_rgbsensor_b.data = random.randrange(start=0, stop=4096, step=1)

        #msg_motor.data = float(random.random())
        #self.robot.Tick(self.i)

        self.topic_01.publish(msg_amotorspeed)
        self.topic_02.publish(msg_amotordeg)
        self.topic_03.publish(msg_bmotorspeed)
        self.topic_04.publish(msg_bmotordeg)
        self.topic_05.publish(msg_cmotorspeed)
        self.topic_06.publish(msg_cmotordeg)
        self.topic_07.publish(msg_ultrasonicraw)
        self.topic_08.publish(msg_touchsensor)
        self.topic_09.publish(msg_rgbsensor_r)
        self.topic_10.publish(msg_rgbsensor_g)
        self.topic_11.publish(msg_rgbsensor_b)
        #self.publisher_ul.publish(msg_ul)
        #self.get_logger().info('---------------------------------------')
        self.get_logger().info(f'[{self.i}]Publishing topic_01: "{msg_amotorspeed.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_02: "{msg_amotordeg.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_03: "{msg_bmotorspeed.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_04: "{msg_bmotordeg.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_05: "{msg_cmotorspeed.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_06: "{msg_cmotordeg.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_07: "{msg_ultrasonicraw.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_08: "{msg_touchsensor.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_09: "{msg_rgbsensor_r.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_10: "{msg_rgbsensor_g.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_11: "{msg_rgbsensor_b.data}"')
        
        #self.get_logger().info('---------------------------------------')
        self.i += 1



def main(args=None):
    rclpy.init(args=args)

    robot = Robot()

    rclpy.spin(robot)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robot.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()