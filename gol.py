#!/usr/bin/env python
import sys
class gol_state(object):
	dead = '.'
	live = '@'
	def __init__(self, gridsize=10):
		#initialise grid
		self.gridsize = gridsize
		self.grid = [ ([self.dead]*self.gridsize) for i in range(self.gridsize)]
	def add_life(self, i, j):
		self.grid[i][j] = self.live
	def show_grid(self):
		for i in range(self.gridsize):
			for j in range(self.gridsize):
				#print self.grid[i][j]
				sys.stdout.write(self.grid[i][j])
			sys.stdout.write("\n")
	def tick(self):
		newgrid = [ ([self.dead]*self.gridsize) for i in range(self.gridsize)]
		for i in range(self.gridsize):
			for j in range(self.gridsize):
				score = 0
				for x,y in [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]:
					try:
						score += 1 if (self.grid[x][y] == self.live) else 0
					except:
						pass
				if ((score == 3) and (self.grid[i][j] == self.dead)):
					newgrid[i][j] = self.live
				elif ((score == 3 or score == 2) and (self.grid[i][j] == self.live)):
					newgrid[i][j] = self.live
				else:
					newgrid[i][j] = self.dead
		self.grid = newgrid


if (__name__ == "__main__"):

	g = gol_state()
	g.add_life(0,1)
	g.add_life(1,2)
	g.add_life(2,0)
	g.add_life(2,1)
	g.add_life(2,2)
	g.show_grid()

	for i in range(10):
		raw_input()
		g.tick()
		g.show_grid()
		
