from time import sleep
# from .._internal.tello import Tello
from tellopy import Tello

# dig through the import line, need the Tello() in \_internal/tello.py


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
        # drone.combined_motion(50, 0, 50, 0, 0, 0, 0, 0)
        # sleep(5)
        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()
