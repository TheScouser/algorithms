def palindrome_perm(string):
	char_count = {}
	odd_count = 0
	for i in range(len(string)):
		if string[i] == ' ':
			continue
		char_count[string[i]] = char_count.get(string[i],0) + 1

	for key,value in char_count.iteritems():
		print key,value
		if value  % 2 != 0:
			odd_count += 1
		if odd_count > 1:
			return False
	return True

print palindrome_perm("taco cat")