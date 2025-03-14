#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import colorsys as cs
from matplotlib import colors

def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    #rc('text', usetex=True) 
    #rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)


    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.pdf')

#Funkcja z wykładu
def hsv2rgb(h, s, v):
    """
    - H: Hue [0,1]
    - S: Saturation [0,1]
    - V: Value [0,1]
    
    """
    h = h * 360  # Convert H to degrees (0 to 360)

    #1. If S = 0 the colour is a shade of grey and RGB are set to V
    if s == 0:
        return (v, v, v)
    
    #2. If S > 0 the following rules:
    Hi = int(h / 60) 
    f = (h / 60) - Hi
    P = v * (1 - s)  
    q = v * (1 - s * f) 
    t = v * (1 - s * (1 - f))

    if Hi == 0: # 0 - 60
        r, g, b = v, t, P
    elif Hi == 1: # 60 - 120
        r, g, b = q, v, P
    elif Hi == 2: # 120 - 180
        r, g, b = P, v, t
    elif Hi == 3: # 180 - 240
        r, g, b = P, q, v
    elif Hi == 4: # 240 - 300
        r, g, b = t, P, v
    else:  # Hi == 5 (300 - 360)
        r, g, b = v, P, q

    # Clamp values to the range [0, 1]
    r = max(0, min(1, r))
    g = max(0, min(1, g))
    b = max(0, min(1, b))

    return (r, g, b)


def gradient_rgb_bw(v):
    return (v, v, v)

def gradient_rgb_gbr(v):
    if v <= 0.5:
        return (0, 1-2*v, 2*v)
    else:
        v-=0.5
        return(2*v,0,1-2*v)

def gradient_rgb_gbr_full(v):
    if v < 0.25: # Green -> Cyan
        return (0, 1, 4*v)  
    elif v < 0.5: # Cyan -> Blue        
        return (0, 2-4*v, 1)  
    elif v < 0.75: # Blue -> Magenta
        return (4*v-2, 0, 1) 
    else: # Magenta -> Red
        return (1, 0, 4-4*v) 

def gradient_rgb_wb_custom(v):
    if v < 0.1:  # White -> Pink
        r = 1
        g = 1 - 10 * v
        b = 1
    elif v < 0.24:  # Pink -> Blue 
        r = 1 - 10 * (v - 0.14)
        g = 0
        b = 1
    elif v < 0.42:  # Blue -> Cyan 
        r = 0
        g = 10 * (v - 0.3) 
        b = 1  
    elif v < 0.55:  # Cyan -> Green
        r = 0
        g = 1 
        b = 1 - 10 * (v - 0.4)
    elif v < 0.65:  # Green -> Yellow
        r = 10* (v - 0.55)
        g = 1
        b = 0
    elif v < 0.85:  # Yellow -> Red
        r = 1
        g = 1 - 6.65 * (v - 0.65)
        b = 0.5 * (0.85 - v)
    else:  # Red -> Black
        r = 1 - 6.67 * (v - 0.85)
        g = 0
        b = 0

    # Clamp the values to the range [0, 1]
    r = max(0, min(1, r))
    g = max(0, min(1, g))
    b = max(0, min(1, b))

    return (r, g, b)

def gradient_hsv_bw(v):
    return cs.hsv_to_rgb(0, 0, v)

def gradient_hsv_gbr(v):

    h = 120 + (v * 240)
    return hsv2rgb(h / 360, 1, 1)

def gradient_hsv_unknown(v):
    h = 120 - (v * 120)
    return hsv2rgb(h / 360, 0.5, 1)


def gradient_hsv_custom(v):

    h = v * 360
    s = 1-  v      
    return hsv2rgb(h / 360, 1-v, 1)




if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
