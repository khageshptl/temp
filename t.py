#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_format = '%a %d %b %Y %H:%M:%S %z'
    date_1 = datetime.strptime(t1, date_format)
    date_2 = datetime.strptime(t2, date_format)
    
    time_diff = date_2 - date_1
    
    diff_in_sec = time_diff.total_seconds()
    
    return diff_in_sec
    
if __name__ == '__main__':
    fptr = open(os.environ['p1.txt'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
