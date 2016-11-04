class Node:
	def __init__(self,element,next):
		self.element = element
		self.next = next

	def __str__(self):
		return str(self.element)

class LinkedList:
	def __init__(self):
		self.size = 0
		self.head = None

	def is_empty(self):
		return self.size == 0

	def add_front(self,element):
		self.head = Node(element,self.head)
		self.size+=1

	def remove_front(self):
		if not self.is_empty():
			self.head = self.head.next

	def get(self,index):
		if self.size < index or index > self.size:
			return None

		current = self.head
		for i in range(0,index):
			current = current.next
		return current.element

		
	# def reverse(self):
	# 	prev = None
	# 	current = self.head
	# 	while current:
	# 		next = current.get_next()
	# 		current.set_next(prev)
	# 		prev = current
	# 		current = next
	# 	self.head = prev

	def reverse(self):
		reversed_list = LinkedList()
		current = self.head
		while current:
			reversed_list.add_front(current.element)
			current = current.next
		return reversed_list


if __name__ == '__main__':
	ll = LinkedList()
	ll.add_front("1")
	ll.add_front("2")
	ll.add_front("3")
	ll.add_front("4")
	ll.add_front("5")
	l2 = ll.reverse()
	print l2.get(1)