import random
import matplotlib.pyplot as plt

TSLOTS = 100000

class classNode:
	def __init__(self, ttl):
		self.ttl = ttl # slots left until retransmission
	def tick(self):
		self.ttl = self.ttl - 1


def main():
	random.seed()

	for window_size in [8, 16, 32]:
		Nlist = []
		selist = []
		print "Window size: {0:2d}".format(window_size)

		for N in range(1, 33):
			snode = [ classNode(random.randrange(0, window_size)) for _ in range(N) ]
			successful_slots = 0
			slot_efficiency = 0
	
			for slot in range(TSLOTS):
				transmitted_nodes = []
	
				for i in range(N):
					if not snode[i].ttl:
						transmitted_nodes.append(i)
						snode[i].ttl = random.randrange(0, window_size)
					else:
						snode[i].tick()
	
				if not transmitted_nodes:
					pass
	
				if (len(transmitted_nodes) == 1):
					successful_slots = successful_slots + 1
				
				if (len(transmitted_nodes) > 2):
					for j in transmitted_nodes:
						snode[j].ttl = random.randrange(0, window_size)
				
			slot_efficiency = (successful_slots/float(TSLOTS))
	
			print "N = {0:2d}: {1:f}".format(N, slot_efficiency)
			
			Nlist.append(N)
			selist.append(slot_efficiency)
		
		plt.plot(Nlist, selist)
		print ""

	plt.xlabel("# of Nodes")
	plt.ylabel("Slot Efficiency")
	plt.legend(['W = 8', 'W = 16', 'W = 32'], loc='upper right')
	plt.axis([0, 32, 0, 1])
	plt.grid(linestyle='--')
	plt.show()

	return


if __name__ == "__main__":
	main()
