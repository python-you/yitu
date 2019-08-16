import threading
import time

event = threading.Event()


def lighter():
    count = 0
    event.set()
    while True:
        if 5 < count < 10:
            event.clear()
            print("red light is on")
        elif count > 10:
            count = 0
            event.set()
        else:
            print("green light is on")
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():
            print("the light is green,%s is running" % name)
            time.sleep(2)
        else:
            print("the traffic light is red, %s should be stopped" % name)
            event.wait()
            print("the light is green,%s start to running" % name)


light = threading.Thread(target=lighter, )
light.start()
car = threading.Thread(target=car, args=('Mercedeze Benze',))
car.start()