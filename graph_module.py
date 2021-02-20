class graph:
	
	dict={}
	nodeLabel={}
	nodeEcc={}
	
	def addArc(self,node,neighbour):
		if node not in self.dict:
			self.dict[node]=[neighbour]
		else:
			self.dict[node].append(neighbour)
			
	def addEdge(self,node,neighbour):
		self.addArc(node, neighbour)
		self.addArc(neighbour, node)
			
	#Really useless algs
	def find_path(self,start,end,path=[]):
		path = path + [start]    
		if start==end:
			return path
		for node in self.dict[start]:
			if node not in path:
				newPath=self.find_path(node,end,path)
				if newPath:
					return newPath
				return None       
	
	def show_edges(self):
		for node in self.dict:
			for neighbour in self.dict[node]:
				print("(", node, ",", neighbour,")")
				
	def BFS(self,t):
		s=t
		visited={}
		
		for i in self.dict:
			visited[i]=False
			self.nodeLabel[i]=-1
		self.nodeLabel[s]=e=0
		queue=[]
		queue.append(s)       
		visited[s]=True
		while len(queue)!=0:
			s=queue.pop(0)
			for node in self.dict[s]:
				if visited[node]==False:
					visited[node]=True
					self.nodeLabel[node]=self.nodeLabel[s]+1
					if self.nodeLabel[node] > e:
						e=self.nodeLabel[node]
					queue.append(node)
			#print(s, end=" ")
		self.nodeEcc[t]=e
		
	def mBFS(self,sources):
		visited={}
		
		for i in self.dict:
			visited[i]=False
			self.nodeLabel[i]=-1
			
		for node in sources:
			visited[node]=True
			self.nodeLabel[node]=0
		e=0
		
		queue=sources
		
		while len(queue)!=0:
			s=queue.pop(0)
			for node in self.dict[s]:
				if visited[node]==False:
					visited[node]=True
					self.nodeLabel[node]=self.nodeLabel[s]+1
					if self.nodeLabel[node] > e:
						e=self.nodeLabel[node]
					queue.append(node)

	def distance(self, start, end):
		self.BFS(start)
		return self.nodeLabel[end]
		
	def trace(s):
		self.BFS(s)
		ring = [[] for i in range(7)]
		#ring[i] adalah list orang yang berjarak i dari epicenter
		#i==0 adalah epicenter
		#ring[6] untuk semua ring i>5
	
		for x in self.dict:
			ring[self.nodeLabel[x]].append(x)
		
		return ring
	
	
	def mtrace(s):
		for x in s:
			if x not in self.dict:
				return 'Data %s tidak ditemukan didalam graf' %x
	
		self.mBFS(s)
		ring = [[] for i in range(7)]
		#ring[i] adalah list orang yang berjarak i dari epicenter
		#i==0 adalah epicenter
		#ring[6] untuk semua ring i>5
	
		for x in self.dict:
			ring[self.nodeLabel[x]].append(x)
		
		return ring
	
	'''	
	def dijkstra(self, start, end):
		
		queue = []
		visited={}
		dist={}
		prev={}
		path=[]
		
		for node in self.dict:
			visited[node]=False
			dist[node]=len(self.dict)+1
			prev[node]=''
			queue.append(node)
			
		dist[start]=0
		
		while visited[end]==False:
			s=queue.pop(0)
			visited[s]=True
			for node in self.dict[s]:
				if visited[node]==False:
					dist[node]=dist[s]+1
					prev[node]=s
					queue.append(node)
		
		s=end
		while s != start:
			path.append(s)
			s=prev[s]
		
		return path
		'''
		
		
