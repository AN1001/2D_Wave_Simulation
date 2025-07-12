import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
plt.ion() #possibly needed for macos
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(12, 5))

#X and Y positions of the IMUs 
imu1_x, imu1_y = 1, 1
imu2_x, imu2_y = 1.5, 1.5
imu3_x, imu3_y = 1.3, 2

#Physical constants 
L_x = 4.0
L_y = 4.0
dx = 0.01
c = 0.5
dt = 0.707*dx/c

x = np.arange(0,L_x*(1+dx),dx)
y = np.arange(0,L_y*(1+dx),dx)
X,Y = np.meshgrid(x,y)

Z = np.zeros((3,len(y),len(x)))

#initialise Gaussian Pulse 
center, stretch = 2, 0.05
Z[0,:,:] = np.exp(-((X-center)/stretch)**2)*np.exp(-((Y-center)/stretch)**2)

#first time step
Z[1,1:-1,1:-1] = Z[0,1:-1,1:-1]+0.5*c**2*(dt**2/dx**2)*(Z[0,1:-1,2:]+Z[0,1:-1,:-2]-2*Z[0,1:-1,1:-1])\
                               +0.5*c**2*(dt**2/dx**2)*(Z[0,2:,1:-1:]+Z[0,:-2,1:-1]-2*Z[0,1:-1,1:-1])

nsteps = 621
imu1_reading, imu2_reading, imu3_reading = [], [], []
mesh = ax1.pcolormesh(X, Y, Z[0], vmin=-0.1, vmax=0.1)
ax1.set_aspect('equal')
ax1.set_title('Wave Simulation')
for coords in [(imu1_x, imu1_y), (imu2_x, imu2_y), (imu3_x, imu3_y)]:
    rect = patches.Rectangle(coords, 0.01, 0.01, linewidth=1, edgecolor='black', facecolor='none')
    ax1.add_patch(rect)

line1 = ax2.plot([], [])[0]
line2 = ax3.plot([], [])[0]
line3 = ax4.plot([], [])[0]
for i,ax in enumerate([ax2, ax3, ax4]):
    ax.set_title(f'IMU {i+1} Reading')
    ax.set_xlim(0, nsteps*dt-dt)
    ax.set_ylim(-0.1, 0.1)

plt.tight_layout()


for i in range(nsteps):
    #compute extra boundary conditions
    #Z[1,130,20:100] = 0

    Z[2,1:-1,1:-1] = -Z[0,1:-1,1:-1] + 2*Z[1,1:-1,1:-1] + c**2*(Z[1,1:-1,:-2]+Z[1,1:-1,2:]-2*Z[1,1:-1,1:-1])*(dt**2/dx**2) + c**2*(Z[1,:-2,1:-1]+Z[1,2:,1:-1]-2*Z[1,1:-1,1:-1])*(dt**2/dx**2) 
    
    #resistive forces
    Z[2,:,:]*=0.99

    Z[0,:,:] = Z[1,:,:]
    Z[1,:,:] = Z[2,:,:]

    imu1_reading.append(Z[2,int(imu1_y/dx),int(imu1_x/dx)])
    imu2_reading.append(Z[2,int(imu2_y/dx),int(imu2_x/dx)])
    imu3_reading.append(Z[2,int(imu3_y/dx),int(imu3_x/dx)])

    # only draw every 5th time step (reduce for smoother but slower animation)
    if i % 5 == 0:
        mesh.set_array(Z[2].ravel())
        line1.set_data(np.linspace(0, (len(imu1_reading)-1)*dt, len(imu1_reading)), imu1_reading)
        line2.set_data(np.linspace(0, (len(imu2_reading)-1)*dt, len(imu2_reading)), imu2_reading)
        line3.set_data(np.linspace(0, (len(imu3_reading)-1)*dt, len(imu3_reading)), imu3_reading)
        
        plt.pause(0.001)

input("Simulation complete, type any character to end program > ")
