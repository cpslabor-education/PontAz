#!/usr/bin/env python3

# Ev3Dev Self driving robot classified
# Last edit 2021.12.04 by CCCompiler


# Import packages

import ev3dev2
import time
import threading

# Using ir_sensor or ul_sensor
SENSOR_TYPE = "ul_sensor"

class self_drive():

    def __init__(self):
        self.isInitialized = False
        self._running = False
        
        self._headMotor = ev3dev2.motor.MediumMotor(ev3dev2.motor.OUTPUT_C)
        self._leftDriveMotor = ev3dev2.motor.LargeMotor(ev3dev2.motor.OUTPUT_B)
        self._rightDriveMotor = ev3dev2.motor.LargeMotor(ev3dev2.motor.OUTPUT_A)

        self._headSensor = None
        if SENSOR_TYPE == "ir_sensor":
            self._headSensor = ev3dev2.sensor.lego.InfraredSensor()
        elif SENSOR_TYPE == "ul_sensor":
            self._headSensor = ev3dev2.sensor.lego.UltrasonicSensor()
        else:
            raise ValueError('SENSOR_TYPE is ir_sensor or ul_sensor only')
        
        self._leds = ev3dev2.led.Leds()

        self._speaker = ev3dev2.sound.Sound()

        self._touchSensor = ev3dev2.sensor.lego.TouchSensor()

        self._sper = ev3dev2.motor.SpeedPercent

        self._driving_value = 0
        self._driving_position = 0
        self._current_proximity = 0
        self._target_proximity = 20
        self._slow_proximity = 3
        self._fast_proximity = 20

        self._head_next_pos_res = 20  # The resolution of the next value
        self._head_next_pos_val = 100 # The head move to one side in degs
        self._head_next_pos = []

        self._head_neg_boundle_low   = -1
        self._head_neg_boundle_high  = -100
        self._head_pos_boundle_low   = 1
        self._head_pos_boundle_high  = 100

        self._normal_driving_speed = 20
        self._turn_driving_speed = 50


        self._time = time

    def setup(self):

        print('Initializing...')
        self._speaker.play_file('cucc.wav')
        self._leds.set_color("LEFT", "ORANGE")
        self._leds.set_color("RIGHT", "ORANGE")

        for _ in range(int(self._head_next_pos_val/self._head_next_pos_res)):
            self._head_next_pos.append(int(self._head_next_pos_res))
        for _ in range(int(2*(self._head_next_pos_val/self._head_next_pos_res))):
            self._head_next_pos.append(int(-self._head_next_pos_res))
        for _ in range(int(self._head_next_pos_val/self._head_next_pos_res)):
            self._head_next_pos.append(int(self._head_next_pos_res))
        
        self._head_next_pos_total = 4*(self._head_next_pos_val/self._head_next_pos_res)

        self._iter = 0

        self._headMotor.stop_action = "coast"
        self._headMotor.speed_sp = self._fast_proximity

        self._t1 = threading.Thread(target=self.driving)

        self._time.sleep(1)

        self._leds.set_color("LEFT", "GREEN")
        self._leds.set_color("RIGHT", "GREEN")

    def loop(self):
        self._running = True
        self._t1.daemon = True
        self._t1.start()

        while not self._touchSensor.is_pressed and self._running:
            self._iter = 0 if self._iter == self._head_next_pos_total else self._iter

            print("iter: ", self._iter,\
                  "head_next_pos: ", self._head_next_pos[self._iter],\
                  "headMotor.position: ", self._headMotor.position)

            power = self._slow_proximity if self._current_proximity < self._target_proximity else self._fast_proximity
            self._headMotor.on_for_degrees(self._sper(power),\
                self._head_next_pos[self._iter],\
                brake=False,\
                block=False
            )

            if SENSOR_TYPE == "ir_sensor":
                self._current_proximity = self._headSensor.proximity
            elif SENSOR_TYPE == "ul_sensor":
                self._current_proximity = self._headSensor.disstance_centimeters
            else:
                raise ValueError('SENSOR_TYPE is ir_sensor or ul_sensor only')

            self._driving_position = self._headMotor.position
            print("headSensor: ", self._current_proximity,\
                  "headPosition: ", self._driving_position)
            self._driving_value = self.calculate_dir(self._head_neg_boundle_low,\
                                                     self._head_neg_boundle_high,\
                                                     0,\
                                                     self._target_proximity,\
                                                     self._head_pos_boundle_low,\
                                                     self._head_pos_boundle_high,\
                                                     self._current_proximity,\
                                                     self._driving_position)
            
            print("driving_value: ", self._driving_value,\
                  "driving_position: ", self._driving_position)
            
            self._iter += 1
            self._time.sleep(0.001)
        self._running = False

    def clear(self):
        self._leds.set_color("LEFT", "RED")
        self._leds.set_color("RIGHT", "RED")
        self._headMotor.position_sp = 0
        self._headMotor.speed_sp = self._fast_proximity
        self._headMotor.stop_action = 'hold'
        self._headMotor.run_to_abss_pos()
        self._time.sleep(1)
        
        self._leftDriveMotor.off()
        self._rightDriveMotor.off()
        self._leds.set_color("LEFT", "GREEN")
        self._leds.set_color("RIGHT", "GREEN")

    def driving(self):
        self._leftDriveMotor.stop_action = "coast"
        self._rightDriveMotor.stop_action = "coast"

        while self._running:
            if self._driving_value == 0:
                self._leftDriveMotor.on(self._sper(self._normal_driving_speed), brake=False, block=False)
                self._rightDriveMotor.on(self._sper(self._normal_driving_speed), brake=False, block=False)
            elif self._driving_value == 1:
                self._rightDriveMotor.on(self._sper(-self._turn_driving_speed), brake=False, block=False)
                self._leftDriveMotor.on(self._sper(self._driving_position), brake=False, block=False)
                if self._current_proximity < self._target_proximity:
                    speed = (self._current_proximity-30)
                    self._rightDriveMotor.on(self._sper(speed), brake=False, block=False)
                    self._leftDriveMotor.on(self._sper(speed), brake=False, block=False)
            elif self._driving_value == -1:
                self._leftDriveMotor.on(self._sper(-self._turn_driving_speed), brake=False, block=False)
                self._rightDriveMotor.on(self._sper(self._driving_position), brake=False, block=False)
                if self._current_proximity < self._target_proximity:
                    speed = (self._current_proximity-30)
                    self._leftDriveMotor.on(self._sper(speed), brake=False, block=False)
                    self._rightDriveMotor.on(self._sper(speed), brake=False, block=False)

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


def main():
    robot = self_drive()
    robot.setup()
    robot.loop()
    robot.clear()


if __name__ == "__main__":
    main()