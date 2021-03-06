#Author: Nandini Patel
#Date: May 05, 2020
#Description: Understanding dates and time

import time
from time import time as my_timer
import random

print(time.gmtime(0))
print(time.localtime())
print(time.time())

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")
end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Reaction time was {} seconds".format(end_time-start_time))