import json
#from dummyHoloData import Hololive
from graph_module import graph

def writedatajson(data):
	with open('data.json', 'w') as f:
		json.dump(data, f, indent=4)
		
def updatedatajson():
	tmp = graph()
	
	with open('data.json', 'r') as f:
		tmp.dict = json.load(f)
	
	tmp.addEdge('a','c')
	print(tmp.dict)
	
	f = open('data.json', 'w')
	json.dump(tmp.dict, f)
	f.close()
	
	
if __name__=='__main__':
	
	data=graph()
	data.dict={
		'a':['b','c'],
		'b':['a'],
		'c':['a']
	}
	#data.addEdge('a','c')
	writedatajson(data.dict)
	#updatedatajson()