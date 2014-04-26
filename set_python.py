import sets_in_python as AbstractSet

class Set(AbstractSet.AbstractSet):
	def __init__(self, elems=()):
		AbstractSet.AbstractSet.__init__(self)
		self.rep = []
		self.insertAll(elems)
		
	def contains(self, a):
		return a in self.rep
		
	def insert(self, a):
		if a not in self.rep:
			self.rep.append(a)
		return self
		
	def delete(self, a):
		if a in self.rep:
			self.rep.remove(a)
		return self
		
	def members(self):
		return self.rep[:]
		
	def new(self):
		return Set()
		
	def copy(self):
		c = Set()
		c.rep = self.rep[:]
		return c
		
	def size(self):
		return len(self.rep)
		
		
obj = Set(("gfbv","fgfg"))

obj2 = Set(["fgfg"])
obj2.insert("object5")
obj2.insert("jjh")
obj2.insert("hghg")
print obj2

obj.insert("object")
obj.insert("jjh")
obj.insert("ttt")
print obj.size()
print obj
obj.delete("jjh")
print obj

obj3 = obj.union(obj2)
print obj3
print obj3.pop()
print obj3