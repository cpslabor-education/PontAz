# 04_Automatic_And_Intelligent_Robots course
#
# robot node: 
# 
# Simulate a robot that has 2 driver motor (A, B) and a head with an ultrasonic sensor
# and a motor (C)
# The node returns a string with the motor's speed/deg and the ultrasonic's 
# sensor raw/real values
# #&@!!
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
# The send and receive functions are dinamycal so you don't need to write a couple of same code
#
#
# Created by: Füleki Tamás 2021.10.20

from numpy.core.fromnumeric import var
import rclpy
from rclpy.node import Node

from webots_controller import Robot

from std_msgs.msg import String,\
                         Float64,\
                         Int32,\
                         Bool,\
                         Int8
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def myMap(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)



class Pid(Node):

    def __init__(self):
        super().__init__('pid')
        
        #subscription = node.create_subscription(
        #String, 'topic', lambda msg: node.get_logger().info('I heard: "%s"' % msg.data), 10)

        # Init subscribers

        self.sub_01 = self.create_subscription(Float64, 'get_amotorspeed', self.listener_callback_as, 10)
        self.sub_02 = self.create_subscription(Float64, 'get_amotordeg', self.listener_callback_ad, 10)
        self.sub_03 = self.create_subscription(Float64, 'get_bmotorspeed', self.listener_callback_bs, 10)
        self.sub_04 = self.create_subscription(Float64, 'get_bmotordeg', self.listener_callback_bd, 10)
        self.sub_05 = self.create_subscription(Float64, 'get_cmotorspeed', self.listener_callback_cs, 10)
        self.sub_06 = self.create_subscription(Float64, 'get_cmotordeg', self.listener_callback_cd, 10)
        self.sub_07 = self.create_subscription(Int32, 'get_ultrasonicraw', self.listener_callback_ul, 10)
        self.sub_08 = self.create_subscription(Bool, 'get_touchsensor', self.listener_callback_ts, 10)
        self.sub_09 = self.create_subscription(Int32, 'get_rgbsensor_r', self.listener_callback_cr, 10)
        self.sub_10 = self.create_subscription(Int32, 'get_rgbsensor_g', self.listener_callback_cg, 10)
        self.sub_11 = self.create_subscription(Int32, 'get_rgbsensor_b', self.listener_callback_cb, 10)
        
        # Init publishers

        self.pub_01 = self.create_publisher(Int8, 'set_direction', 10)
        self.pub_02 = self.create_publisher(Float64, 'set_speed', 10)
        self.pub_03 = self.create_publisher(Int32, 'set_ul_real', 10)

        self.timer = self.create_timer(0.2, self.compute_data)

        #self.sub_01  # prevent unused variable warning
        
        self._as = [0]
        self._ad = [0]
        self._bs = [0]
        self._bd = [0]
        self._cs = [0]
        self._cd = [0]
        self._ul = [0]
        self._ts = [0]
        self._cr = [0]
        self._cg = [0]
        self._cb = [0]
        #plt.show(block=True)

    def listener_callback_as(self, msg):
        self._as.append(msg.data)
        self._as = self._as[-9:]
    def listener_callback_ad(self, msg):
        self._ad.append(msg.data)
        self._ad = self._ad[-9:]
    def listener_callback_bs(self, msg):
        self._bs.append(msg.data)
        self._bs = self._bs[-9:]
    def listener_callback_bd(self, msg):
        self._bd.append(msg.data)
        self._bd = self._bd[-9:]
    def listener_callback_cs(self, msg):
        self._cs.append(msg.data)
        self._bd = self._bd[-9:]
    def listener_callback_cd(self, msg):
        self._cd.append(msg.data)
        self._cd = self._cd[-9:]
    def listener_callback_ul(self, msg):
        self._ul.append(msg.data)
        self._ul = self._ul[-9:]
    def listener_callback_ts(self, msg):
        self._ts.append(msg.data)
        self._ts = self._ts[-9:]
    def listener_callback_cr(self, msg):
        self._cr.append(msg.data)
        self._cr = self._cr[-9:]
    def listener_callback_cg(self, msg):
        self._cg.append(msg.data)
        self._cg = self._cg[-9:]
    def listener_callback_cb(self, msg):
        self._cb.append(msg.data)
        self._cb = self._cb[-9:]

    def sendPub(self, where, type, msg):
        obj = type()
        obj.data = msg
        #method = getattr(Pid.__init__, where)
        #print(type(where))
        where.publish(obj)



    def computeLogger(self, variables, command, names=None, ret=None): # self, variable, command
        #arg_list = [*args]
        #variable = arg_list[0]
        #command = arg_list[1]
        for variable, name in zip(variables, names):
            last_read_data = variable[-1:]
        #var_name = f'{variable=}'.partition('=')[0]
        #var_name = [ i for i, a in locals().items() if a == variable][0]
        #var_name = str(arg_list[0])
            self.get_logger().info(f'Last read data of {name}: "{last_read_data}"')
            self.get_logger().info(f'Data of {name}: "{variable}"')
            avg_of_read_data = np.average(variable)
            self.get_logger().info(f'Avg of read data: "{avg_of_read_data}"')
            trans_data = command(variables)
            self.get_logger().info(f'Trans data of {name}: "{trans_data}"')
            self.get_logger().info('--------------------------------------------------------------------------')

        if ret != None:
            self.get_logger().info('Response sent!')
            if ret.__len__() > 1:
                for i in range(ret.__len__()):
                    ret[i][0](ret[i][1], ret[i][2], trans_data[i])
            else:
                ret[0][0](ret[0][1], ret[0][2], trans_data)
        

    def ul_raw_to_real(self, raw):
        return int(myMap(raw, 0.0, 4096.0, 0.0, 255.0))

    def get_degrees_and_distance(self, variables):
        neg_low = -180
        neg_high = -1
        pos_low = 1
        pos_high = 180
        ul_min = 0
        ul_max = 25
        d_v = 0
        ul_real = self.ul_raw_to_real(variables[1][-1])
        low_b = 1 if variables[0][-1] > neg_low and variables[0][-1] < neg_high else 0
        high_b = 1 if variables[0][-1] > pos_low and variables[0][-1] < pos_high else 0
        d_v = 1 if ul_real > ul_min and ul_real < ul_max else 0
        l_n_v = 1 if d_v and low_b else 0
        h_n_v = 1 if d_v and high_b else 0
        i = l_n_v - h_n_v
        if i == 1:
            #return "Left_Back_at_"+str(variables[0][-1])+"_speed"
            return (1, variables[0][-1]-30.0, ul_real)
        elif i == -1:
            #return "Right_Back_at_"+str(variables[0][-1])+"_speed"
            return (-1, variables[0][-1]-30.0, ul_real)
        elif i == 0:
            #return "Back_at_"+str(variables[0][-1])+"_speed"
            return (0, variables[0][-1]-30.0, ul_real)
        else:
            #return "Straight"
            return (3, 100.0, ul_real)




    def compute_data(self):
        #last_read_data_as = self._as[-1:]
        #self.get_logger().info(f'Last read data: "{last_read_data_as}"')
        #avg_of_last_read_data_as = np.average(self._as)
        #trans_data = (now_data*2)
        #self.get_logger().info(f'Avg of read data: "{avg_of_last_read_data_as}", len: "{self._as.__len__()}"')
        #self.get_logger().info(f'Last 10 item:{self._as}')

        self.computeLogger(
            [self._as], 
            lambda x: 1 if x[0][-1] > 50 else 0 if x[0][-1] < -50 else 1, 
            names=["_as"]
        )
        self.computeLogger(
            [self._ts],
            lambda x: "Pressed" if x[0][-1] else "Released",
            names=["_ts"]
        )
        self.computeLogger(
            [self._cr, self._cg, self._cb], 
            lambda x: "White" if x[0][-1] > 200 and x[1][-1] > 200 and x[2][-1] > 200 else "Black"\
                      if x[0][-1] < 50 and x[1][-1] < 50 and x[2][-1] < 50 else "Blue", 
            names=["R", "G", "B"]
        )
        self.computeLogger(
            [self._cd, self._ul],
            self.get_degrees_and_distance,
            names=["Head"],
            ret=[[self.sendPub, self.pub_01, Int8],
                 [self.sendPub, self.pub_02, Float64],
                 [self.sendPub, self.pub_03, Int32]
            ]
        )
    
        





def main(args=None):
    rclpy.init(args=args)

    pid = Pid()
    rclpy.spin(pid)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pid.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()