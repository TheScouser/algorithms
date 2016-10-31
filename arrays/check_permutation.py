import unittest

def sort_string(string):
	char_array = [char for char in string]
	char_array.sort()
	return "".join(char_array)

def check_permutation(str1,str2):
	if len(str1) != len(str2):
		return False

	return sort_string(str1) == sort_string(str2)


class PermutationTest(unittest.TestCase):
	def test_no_permutation(self):
		self.assertFalse(check_permutation("bla","abc"))

	def test_permutation_1(self):
		self.assertTrue(check_permutation("abc","cba"))

	def test_no_permutation_2(self):
		self.assertFalse(check_permutation("blds","cba"))

if __name__ == '__main__':
	unittest.main()