from time import sleep
# from .._internal.tello import Tello
from tellopy import Tello


def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


def test():
    drone = Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)

        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(5)
        # drone.combined_motion(up, down, left, right, forward, backward, cw, ccw)
        drone.combined_motion(0, 10, 0, 0, 20, 0, 0, 50)
        # drone.combined_motion()
        sleep(5)
        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()
