import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Animation(object):

	def __init__(self, states, xlim=(0,100), ylim=(0,100)):
		
		self.xlim = xlim
		self.ylim = ylim
		self.frames = [(0,50),(25,50),(50,50),(75,50),(100,50)]

		self.fig, self.ax = plt.subplots()
		self.ln, = plt.plot([], [], 'ro', animated=True)

		

	def runAnimation(self):
		
		def init():
			    self.ax.set_xlim(*self.xlim)
			    self.ax.set_ylim(*self.ylim)
			    return self.ln,

		def update(frame):
		    xdata = [frame[0]]
		    ydata = [frame[1]]
		    self.ln.set_data(xdata, ydata)
		    return self.ln,

		ani = FuncAnimation(self.fig, update, frames=self.frames,
		                    init_func=init, blit=True)
		plt.show()

		

states = [[0]*10, [1]*10, [2]*10]
A = Animation(states)
A.runAnimation()



