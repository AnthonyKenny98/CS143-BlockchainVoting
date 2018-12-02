import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from network import simpleSimulation

class Animation(object):

	def __init__(self, states, xlim=(0,10), ylim=(0,10)):
		
		self.xlim = xlim
		self.ylim = ylim
		self.frames = states
		self.fig, self.ax = plt.subplots()
		self.ln, = plt.plot([], [], 'ro', animated=True)
		self.xdata, self.ydata = [], []
		

	def runAnimation(self):
		
		def init():
			    self.ax.set_xlim(*self.xlim)
			    self.ax.set_ylim(*self.ylim)
			    return self.ln,

		def update(frame):
		    node, length = frame
		    if node not in self.ydata:
		    	self.ydata.append(node)
		    	self.xdata.append(length)
		    else:
		    	i = self.ydata.index(node)
		    	self.xdata[i] = length
		    self.ln.set_data(self.xdata, self.ydata)
		    return self.ln,

		ani = FuncAnimation(self.fig, update, frames=self.frames,
		                    init_func=init, blit=True)
		plt.show()

		

states = simpleSimulation()
A = Animation(states)
A.runAnimation()



