
class AbstractSet:
	def contains(self, a):
		raise NotImplementedError, "contains()"
	def insert(self, a):
		raise NotImplementedError, "insert()"
	def delete(self, a):
		raise NotImplementedError, "delete()"
	def members(self):
		raise NotImplementedError, "members()"
	def copy(self):
		raise NotImplementedError, "copy()"
	def new(self):
		raise NotImplementedError, "new()"
	def size(self):
		raise NotImplementedError, "size()"
	
	def __init__(self):
		pass
		
	def insertAll(self, elems):
		for i in elems:
			self.insert(i)
		return self
		
	def pop(self):
		elems = self.members()
		if len(elems) > 0:
			r = elems[0]
			self.delete(r)
			return r
		return None
		
	def union(self, a):
		res = self.copy()
		for i in a.members():
			res.insert(i)
		return res
		
	def intersection(self, a):
		res = self.new()
		for i in self.members():
			if a.contains(i):
				res.insert(i)
		return res
		
	def __str__(self):
		res = self.members()
		return "{"+str(res)[1:-1]+"}"
		
	__repr__ = __str__