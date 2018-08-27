# configure steering
from time import sleep
from tellopy import Tello
# listen to serial port for voltage change across LED (photodiode)




def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


class Steering:
    def __init__(self, drone, signal_strength_gradient):
        self.drone = drone
        self.signal_strength_gradient = signal_strength_gradient

    def steer_left(self):
        self.drone.combined_motion(0,0,0,0,10,0,0,15)

    def steer_right(self):
        self.drone.combined_motion(0,0,0,0,10,0,15,0)

    def steer_straight(self):
        self.drone.combined_motion(0,0,0,0,10,0,0,0)

    def steering_control(self):
        if self.signal_strength_gradient < 0:
            self.steer_left()
        elif self.signal_strength_gradient > 0:
            self.steer_right()
        else:
            self.steer_straight()
class GradChange:
    def __init__(self):

    def

def test():
    drone = Tello()
    steering = Steering(drone, signal_strength_gradient= )
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(5)
        steering.steering_control()
        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()
