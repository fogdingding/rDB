from random import randint, seed
import time
class SkipNode:
	def __init__(self, height = 0, elem = None ,key = None ,url = None ,title = None ,viewCount = None ):
		self.next = [None]*height
		self.elem = elem
		self.key = key
		self.url = url
		self.title = title
		self.viewCount = viewCount
class SkipList:
	def __init__(self):
		self.head = SkipNode()
		self.len = 0
		self.maxHeight = 0

	def __len__(self):
		return self.len

	def randomHeight(self):
		height = 1
		while randint(1, 2)!= 1:
			height += 1
		return height

	def remove(self, elem):
		update = self.updateList(elem)
		x = self.find(elem, update)
		if x != None:
			for i in reversed(range(len(x.next))):
				update[i].next[i] = x.next[i]
				if self.head.next[i] == None:
					self.maxHeight -= 1
			self.len -= 1

	def printList(self):
		for i in range(len(self.head.next)-1, -1, -1):
			x = self.head
			while x.next[i] != None:
				print (x.next[i].elem + '-',end="")
				x = x.next[i]
			print ('')

	def find(self, elem, update = None):
		if update == None:
			update = self.updateList(elem)
		if len(update) > 0:
			candidate = update[0].next[0]
			if candidate != None and candidate.elem == elem:
				return candidate
		return None

	def contains(self, elem, update = None):
		return self.find(elem, update) != None

	def updateList(self, elem):
		update = [None]*self.maxHeight
		x = self.head
		for i in reversed(range(self.maxHeight)):
			while x.next[i] != None and x.next[i].elem < elem:
				x = x.next[i]
			update[i] = x
		return update

	def insert(self, elem, key,url = None ,title = None ,viewCount = None ):
		node = SkipNode(self.randomHeight(), elem, key ,url ,title ,viewCount )
		self.maxHeight = max(self.maxHeight, len(node.next))
		while len(self.head.next) < len(node.next):
			self.head.next.append(None)
		update = self.updateList(elem)            
		if self.find(elem, update) == None:
			for i in range(len(node.next)):
				node.next[i] = update[i].next[i]
				update[i].next[i] = node
			self.len += 1

	def get_ALL(self):
		data = []
		data2 = []
		x = self.head
		while x.next[0] != None:
			data.append(x.next[0].elem)
			data2.append(x.next[0].key)
			x = x.next[0]
		return data,data2
