import network
import time
import gc

print("Booting...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("RaphiHome", "49257960")

print("Waiting for the connection...")
while not wlan.isconnected():
    time.sleep(0.5)

gc.collect()

print("Boot finished!")
