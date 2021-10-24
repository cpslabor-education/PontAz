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
                         Float64MultiArray,\
                         Int8

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
        self.topic_01 = self.create_publisher(Float64, 'get_amotorspeed',    10)
        self.topic_02 = self.create_publisher(Float64, 'get_amotordeg',      10)
        self.topic_03 = self.create_publisher(Float64, 'get_bmotorspeed',    10)
        self.topic_04 = self.create_publisher(Float64, 'get_bmotordeg',      10)
        self.topic_05 = self.create_publisher(Float64, 'get_cmotorspeed',    10)
        self.topic_06 = self.create_publisher(Float64, 'get_cmotordeg',      10)
        self.topic_07 = self.create_publisher(Int32,   'get_ultrasonicraw',  10)
        self.topic_08 = self.create_publisher(Bool,    'get_touchsensor',    10)
        self.topic_09 = self.create_publisher(Int32,   'get_rgbsensor_r',    10)
        self.topic_10 = self.create_publisher(Int32,   'get_rgbsensor_g',    10)
        self.topic_11 = self.create_publisher(Int32,   'get_rgbsensor_b',    10)

        # inintalize subscribers
        self.sub_01 = self.create_subscription(Int8, 'set_direction', self.listen_set_direction, 10)
        self.sub_02 = self.create_subscription(Float64, 'set_speed', self.listen_set_speed, 10)
        self.sub_03 = self.create_subscription(Int32, 'set_ul_real', self.listen_set_ul, 10)

        # self.publisher_ul = self.create_publisher(Float64, 'ul', 10)
        # timer sends packets in every 0.5 seconds
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.computeUp = self.create_timer(0.1, self.computeUp_cr)
        self.i = 0

        # Init local variables

        self._as = 0
        self._ad = 0
        self._bs = 0
        self._bd = 0
        self._cs = 0
        self._cd = 0
        self._ul = 0
        self._ts = 0
        self._cr = 0
        self._cg = 0
        self._cb = 0

        # Init recieved varibles 

        self._l_as = 0
        self._l_bs = 0
        self._l_ul = 0

        self._dir = 0
        self._dir_speed = 0
    
    def genDummyData(self):
        self._as = float(random.randrange(start=-100, stop=100, step=1))
        self._ad = float(random.randrange(start=0, stop=360, step=1))
        self._bs = float(random.randrange(start=-100, stop=100, step=1))
        self._bd = float(random.randrange(start=0, stop=360, step=1))
        self._cs = float(random.randrange(start=-100, stop=100, step=1))
        self._cd = float(random.randrange(start=-180, stop=180, step=1))
        self._ul = random.randrange(start=0, stop=4096, step=1)
        self._ts = bool(random.getrandbits(1))
        self._cr = random.randrange(start=0, stop=4096, step=1)
        self._cg = random.randrange(start=0, stop=4096, step=1)
        self._cb = random.randrange(start=0, stop=4096, step=1)
    
    def listen_set_direction(self, msg):
        self._dir = msg.data
    def listen_set_speed(self, msg):
        self._dir_speed = msg.data
    def listen_set_ul(self, msg):
        self._l_ul = msg.data

    def computeUp_cr(self):
        if self._dir == 1:
            self._l_as = 50
            self._l_bs = self._cd
            if self._l_ul < 25:
                self._l_as = self._dir_speed
                self._l_bs = self._dir_speed
        elif self._dir == -1:
            self._l_as = -50
            self._l_bs = self._cd
            if self._l_ul < 25:
                self._l_as = self._dir_speed
                self._l_bs = self._dir_speed
        elif self._dir == 0:
            self._l_as = -20
            self._l_bs = -20
        else:
            self._l_as = self._dir_speed
            self._l_as = self._dir_speed
        self.get_logger().info(
            f'The robot go "{("Left" if self._dir == 1 else "Right" if self._dir == -1 else "Straight")}"'\
            +f' at {(self._l_as, self._l_bs)} speed'
        )
        

    def timer_callback(self):
        self.genDummyData()
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
        msg_amotorspeed.data = self._as
        msg_amotordeg.data = self._ad
        msg_bmotorspeed.data = self._bs
        msg_bmotordeg.data = self._bd
        msg_cmotorspeed.data = self._cs
        msg_cmotordeg.data = self._cd
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
        msg_ultrasonicraw.data = self._ul
        msg_touchsensor.data = self._ts
        #r = int(random.randrange(0, 4096, 1))
        #g = int(random.randrange(0, 4096, 1))
        #b = int(random.randrange(0, 4096, 1))
        #r = 4096
        #g = 4096
        #b = 4096

        #msg_rgbsensor.data = (r<<24|g<<12|b)
        msg_rgbsensor_r.data = self._cr
        msg_rgbsensor_g.data = self._cg
        msg_rgbsensor_b.data = self._cb

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