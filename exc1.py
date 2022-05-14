from sub.ee import filestring as fs


f = fs()
print(fs.read("res\\1.txt"))
for i in range(10):
	print(f.num(), end=' ')
print()