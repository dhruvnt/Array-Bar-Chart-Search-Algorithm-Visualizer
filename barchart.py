import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

def animated_barplot():
    mu, sigma = 100, 15
    N = 4
    x = mu + sigma*np.random.randn(N)
    rects = plt.bar(range(N), x)
    for i in range(20):
        x = mu + sigma*np.random.randn(N)
        for rect, h in zip(rects, x):
            rect.set_height(h)
        fig.canvas.draw()
        time.sleep(.5)


fig = plt.figure()
win = fig.canvas.manager.window
win.after(100, animated_barplot)
plt.show()