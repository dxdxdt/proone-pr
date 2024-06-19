import random
import uuid


class Node:
	def __init__ (self, id: uuid.UUID = None):
		self.id = id or uuid.uuid4()
		self.childNodes = set[Node]()

def doOutput (n: Node):
	def visit (n: Node, d):
		print(('*' * d) + " " + str(n.id))

		for c in n.childNodes:
			visit(c, d + 1)

	print("@startuml")
	visit(n, 1)
	print("@enduml")

def flag () -> bool:
	# FIXME
	try:
		input()
	except EOFError:
		return False
	return True

root = Node()
l = list[Node]()
l.append(root)

while flag():
	n = random.randrange(0, len(l))
	picked = l[n]

	ny = Node()
	picked.childNodes.add(ny)
	l.append(ny)

	doOutput(root)
