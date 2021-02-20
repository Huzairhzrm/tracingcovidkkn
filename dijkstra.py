from graph_module import graph
#from dummyHoloData import Hololive
import json

#JANGAN LUPA SEBELUM IMPLEMENT HOLOLIVE GANTI SELF!!!
#Hololive = Hololive.graph_dict

with open('testjson.json','r'):
	

def trace(s):
	#self.BFS(s)
	Hololive.BFS(s)
	ring = [[] for i in range(7)]
	#ring[i] adalah list orang yang berjarak i dari epicenter
	#i==0 adalah epicenter
	#ring[6] untuk semua ring i>5
	
	#for x in self.dict:
	for member in Hololive.dict:
		#ring[self.nodeLabel[x]].append(x)
		ring[Hololive.nodeLabel[member]].append(member)
	
	#return ring
	
	#print output
	'''
	for level in range(len(ring)):
		if level==0:
			print('Epicenter:')
		elif level==6:
			print('Zona Aman/Hijau:')
		else:
			print('Ring',level,':')
			
		for person in ring[level]:
			print(person)
	'''
	
def mtrace(s):
	for x in s:
		#if x not in self.dict:
		if x not in Hololive.dict:
			return 'Data %s tidak ditemukan didalam graf' %x
	
	#self.mBFS(s)
	Hololive.mBFS(s)
	ring = [[] for i in range(7)]
	#ring[i] adalah list orang yang berjarak i dari epicenter
	#i==0 adalah epicenter
	#ring[6] untuk semua ring i>5
	
	#for x in self.dict:
	for member in Hololive.dict:
		#ring[self.nodeLabel[x]].append(x)
		ring[Hololive.nodeLabel[member]].append(member)
		
	return ring
	
	#return ring
	
	#print output
	'''
	for level in range(len(ring)):
		if level==0:
			print('Epicenter:')
		elif level==6:
			print('Zona Aman/Hijau:')
		else:
			print('Ring',level,':')
			
		for person in ring[level]:
			print(person)
	'''
	
#trace('Marine')

#def dijkstra(start, end):
	#ToBeImplemented
	
if __name__=='__main__':
	'''
	#Hololive.mBFS(['Suisei','Ayame'])
	Hololive.BFS('Suisei')
	for member in Hololive.nodeLabel:
		print(member, Hololive.nodeLabel[member])
	
	
	path = Hololive.dijkstra('Suisei','Ayame')
	print(path)
	'''
	
	#Test fitur level resiko
	positif=['Suisei','Kanata']
	ring = mtrace(positif)
	
	print('Request Format')
	
	print('Input')
	print()
	obj=input('Nama: ')
	
	print()
	print('Output')
	for level in ring:
		for x in level:
			if x in obj:
				lvl = ring.index(level)
				print('Ring:', lvl)
				if lvl==0:
					print('Risk Level: Positif')
				elif lvl==1 or lvl==2:
					print('Risk Level: Merah')
				elif lvl>=3 and lvl<=5:
					print('Risk Level: Kuning')
				else:
					print('Risk Level: Hijau')
				break
			else:
				continue