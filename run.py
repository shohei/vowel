import os
import time
import math
import random

def rand():
    return int(math.floor(random.random()*12))

while True:
    com = "afplay "+str(rand()+1)+".mp3"
    print com
    os.system(com)
    time.sleep(2)
