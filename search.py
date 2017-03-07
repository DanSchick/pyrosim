from pyrosim import PYROSIM
from robot import ROBOT
import matplotlib.pyplot as plt
import random

for i in range(0, 10):
	sim = PYROSIM(playPaused=False, evalTime = 200)
	robot = ROBOT(sim, random.random() *2 - 1)
	sim.Start()
	sim.Wait_To_Finish()

# sensorData = sim.Get_Sensor_Data(sensorID=2)
# print sensorData

# f = plt.figure()
# pn = f.add_subplot(111)
# plt.plot(sensorData)
# pn.set_ylim(-10,+11)
# plt.show()
