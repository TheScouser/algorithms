import unittest
from collections import defaultdict

def is_unique(string):
	SIZE = 128
	unique_chars = defaultdict(list)
	char_hash = 0

	if len(string) > SIZE:
		return False

	for char in string:
		char_hash = hash(char)
		char_index = char_hash % SIZE
		if (len(unique_chars[char_index]) != 0)  and (unique_chars[char_index][0] == char):
			return False
		unique_chars[char_index].append(char)

	return True

class IsUniqueTest(unittest.TestCase):
	def test_empty(self):
		self.assertTrue(is_unique(""))

	def test_not_unique(self):
		self.assertFalse(is_unique("blaa"))

if __name__ == "__main__":
	unittest.main()