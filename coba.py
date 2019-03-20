
import numpy as np

a = 8
b = 6
c = 3

theta = np.linspace(0, 45 * 2* np.pi, num=10000)
k = (0.8*theta/(2*np.pi)+3)
r = k *(a+np.sin(theta*b+(k/c)))

x = r * np.cos(theta)
y = r * np.sin(theta)

print(theta)