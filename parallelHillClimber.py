from pyrosim import PYROSIM
from robot import ROBOT
from individual import INDIVIDUAL
import matplotlib.pyplot as plt
import random
import copy
import pickle

parent = INDIVIDUAL()
parent.Evaluate(False)
print parent.fitness
for i in range(0, 100):
	child = copy.deepcopy(parent)
	child.Mutate()
	child.Evaluate(True)
	print '[g:', i, '] ', '[pw: ', parent.genome, '] ', '[p:' , parent.fitness , '] ', '[c:', child.fitness, ']'
	if(child.fitness > parent.fitness):
		child.Evaluate(False)
		parent = child
		f = open('robot.p', 'w')
		pickle.dump(parent, f)
		f.close()

# f = plt.figure()
# pn = f.add_subplot(111)
# plt.plot(sensorData)
# pn.set_ylim(-10,+11)
# plt.show()
