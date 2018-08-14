from time import sleep
from tellopy import Tello


def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


def test_case1(drone):
    drone.combined_motion(25, 0, 0, 0, 0, 0, 0, 0)
    sleep(5)
    drone.combined_motion(0, 10, 0, 0, 15, 0, 0, 50)
    sleep(5)
    drone.combined_motion(0, 10, 0, 0, 0, 15, 50, 0)
    sleep(5)
    drone.combined_motion(0, 10, 0, 0, 20, 0, 0, 50)
    sleep(5)
    drone.combined_motion(0, 10, 0, 0, 0, 20, 50, 0)
    sleep(5)
    drone.combined_motion(0, 10, 0, 0, 25, 0, 0, 50)
    sleep(5)
    drone.combined_motion(0, 10, 0, 5, 0, 25, 50, 0)
    sleep(5)


def test_case2(drone):  # smaller arcs
    drone.combined_motion(25, 0, 0, 0, 0, 0, 0, 0)
    sleep(5)
    drone.combined_motion(0, 10, 0, 0, 20, 0, 0, 30)
    sleep(5)
    drone.combined_motion(0, 10, 0, 0, 0, 20, 30, 0)
    sleep(5)
    drone.combined_motion(0, 10, 0, 3, 20, 0, 0, 30)
    sleep(5)
    drone.combined_motion(0, 10, 0, 3, 0, 20, 30, 0)
    sleep(5)
    drone.combined_motion(0, 10, 0, 5, 20, 0, 0, 30)
    sleep(5)
    drone.combined_motion(0, 10, 0, 5, 0, 20, 30, 0)
    sleep(5)


def test():
    drone = Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(5)
        test_case1(drone)
        # combined_motion(up, down, left, right, forward, backward, cw, ccw)
        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()
