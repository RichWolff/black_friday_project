# -*- coding: utf-8 -*-
import numpy as np

def ecdf(data):
    x = np.sort(data)
    n = len(x)
    y = np.arange(1,n+1)/n
    return (x,y)