# 2D_Wave_Simulation
Simulates a 2D (Gaussian pulse) wave and the readings of three IMUs around it in real time.

And then uses the data from the IMUs to try and figure out the location of origin of the pulse (by TDoA).

Can also simulate obstacles with varying levels of absorption (uncomment line below extra boundary conditions)
```python
#obstacle
Z[1,130,20:100] = 0
```
```python
#or only slightly absorb the energy
Z[1,130,20:100] *= 0.8
```
Can adjust any of the starting conditions to change the simulation like `L_x`, `c` or `imu1_x`
Can also adjust size and location of pulse and also frame rate of simulation.

Black dots on plot are IMUs.
Fig1, 3 and 4 are of simulation with resistance upto boundary, 
Fig2 is of simulation without resistance after reflecting off boundary.

![Wave_Simulation](https://github.com/user-attachments/assets/ac7f2b52-2220-4f33-a0f4-5e055c300d61)


<img width="2392" height="990" alt="Simulation Picture" src="https://github.com/user-attachments/assets/edd50539-1375-4b29-807d-8d9bc902b284" />
<img width="2380" height="944" alt="Simulation Picture" src="https://github.com/user-attachments/assets/072adcac-ca05-4032-8dbe-c66e69892fe7" />
<img width="2388" height="982" alt="Screenshot 2025-07-12 at 18 42 37" src="https://github.com/user-attachments/assets/20dcb3bd-fafd-4470-bb69-56549ac1c2b6" />
