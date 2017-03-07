from pyrosim import PYROSIM
from robot import ROBOT
from individual import INDIVIDUAL
import matplotlib.pyplot as plt
import random

for i in range(0, 10):
	individual = INDIVIDUAL()
	individual.Evaluate()
	print individual.fitness
	# sim = PYROSIM(playPaused=False, evalTime = 200)
	# robot = ROBOT(sim, random.random() *2 - 1)
	# sim.Start()
	# sim.Wait_To_Finish()

	# x = sim.Get_Sensor_Data(sensorID=4, s=0)
	# y = sim.Get_Sensor_Data(sensorID=4, s=1)
	# z = sim.Get_Sensor_Data(sensorID=4, s=2)
	# print y[199]

# f = plt.figure()
# pn = f.add_subplot(111)
# plt.plot(sensorData)
# pn.set_ylim(-10,+11)
# plt.show()
