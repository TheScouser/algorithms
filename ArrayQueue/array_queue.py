import unittest

class ArrayQueue:
	def __init__(self,capacity):
		self.queue = [0]  * capacity
		self.capacity = capacity
		self.front = 0
		self.rear = 0
		self.size = 0

	def front(self):
		return self.queue[self.front]

	def is_empty(self):
		return self.size == 0

	def is_full(self):
		return self.size == self.capacity

	def enqueue(self,element):
		if self.is_full():
			raise Exception("Queue is full")

		self.queue[self.rear] = element
		self.rear = (self.rear + 1) % self.capacity
		self.size+=1

	def dequeue(self):
		if self.is_empty():
			raise Exception("Queue is empty")

		element = self.queue[self.front]
		print element
		self.front = (self.front + 1) % self.capacity
		self.size -= 1
		return element


# class TestQueue(unittest.TestCase):
# 	aq = ArrayQueue(10)

# 	def test_enqueue(self	):
# 		self.aq.enqueue(1)
# 		self.assertFalse(self.aq.is_empty())

if __name__ == '__main__':
	# unittest.main()
	aq = ArrayQueue(10)
	aq.enqueue(1)
	print aq.is_empty()