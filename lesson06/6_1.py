from time import sleep

class TrafficLight:
    __color = ["red", "yellow", "green"]

    def running(self):
        while True:
            print('It is red light now. Please, wait.')
            sleep(7)
            print('It is yellow light now. Be ready to start.')
            sleep(2)
            print('It is green light now. Start driving.')
            sleep(5)
            print('It is yellow light now. Get ready to stop.')
            sleep(2)


traffic_light = TrafficLight()
traffic_light.running()