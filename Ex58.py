#!/usr/bin/env python3

from progressbar import progressbar
import time

bar = progressbar(maxvalue = 10)
bar.start()

for i in range(1, 11):
    bar.update(i)
    timesleep(1)

bar.finish
