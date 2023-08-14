import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import numpy as np  

fig, ax = plt.subplots(figsize=(10,5))

ax.set_aspect("equal")
ax.set_xlim(0, 30)
ax.set_ylim(0, 8)
ax.set(xlabel="Sx (m)", ylabel="Sy (m)")

# Constant Value
g = 9.8
theta = np.pi/6.

u = 15
ux = u*np.cos(theta)
uy = u*np.sin(theta)

D = 5

def closet_idx(arr, num):
    return np.argmin(np.abs(np.array(arr)-num))

# A
T1 = np.arange(0, 2*uy/g, 0.05)
x1 = ux*T1
y1 = uy*T1 - (g*T1*T1)/2
meet_index = max(0, closet_idx(T1, D/(ux))-1)

# B
T2 = np.arange(0, 2*uy/g, 0.05)
x2 = ux*T2 + D
y2 = uy*T2 - (g*T2*T2)/2

p1, = ax.plot([], [])
p2, = ax.plot([], [])
frame_number = len(T1)

def update(frame):
    plt.title(f'''
        Projectile Simulation
        Time : {round(T1[-1], 2)} s
        Frame : {frame}
    ''')
    p1.set_data(x1[:frame+1], y1[:frame+1])
    if (frame >= meet_index and frame < frame_number): 
        p2.set_data(x2[:frame-meet_index+1], y2[:frame-meet_index+1])
    else:
        p2.set_data([], [])
    return p1, p2,

ax.axvline(
    (u*u*np.sin(2*theta))/(2*g) + D/2, 
    color="r",
    linestyle="--"
)

animation = FuncAnimation(fig, update, frames=frame_number, interval=100)
animation.save('demo.gif', writer='pillow', fps=60)

plt.show()