from djitellopy import tello
from time import sleep
me = tello.Tello()

me.connect()
print(me.get_battery())
me.takeoff()

sleep(5)

me.land()