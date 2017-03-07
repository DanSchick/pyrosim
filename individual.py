import random
import math
from pyrosim import PYROSIM
from robot import ROBOT


class INDIVIDUAL:
	def __init__(self):
		self.genome = random.random() * 2 - 1
		self.fitness = 0

	def Evaluate(self, pb):
			sim = PYROSIM(playPaused=False, evalTime = 200, playBlind=pb)
			robot = ROBOT(sim, self.genome)
			sim.Start()
			sim.Wait_To_Finish()

			x = sim.Get_Sensor_Data(sensorID=4, s=0)
			y = sim.Get_Sensor_Data(sensorID=4, s=1)
			z = sim.Get_Sensor_Data(sensorID=4, s=2)
			self.fitness =  y[199]
	def Mutate(self):
		self.genome = random.gauss(self.genome, math.fabs(self.genome))
