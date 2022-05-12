class filestring:
	count=0

	def __init__(self):
		self.count=0

	def reverse(ls):
		return ls[::-1]

	def read(dir):
		with open(dir,'r') as f:
			ls = f.readlines()
		return ls

	def num(self):
		self.count+=1
		return self.count