def compress(string):
	compressed = []
	current_char = string[0]
	count = 0
	for i in range(len(string)):
		if current_char != string[i]:
			compressed.append(current_char+str(count))
			count = 0
			current_char = string[i]
			count += 1
		elif i == len(string) - 1:
			count+=1
			compressed.append(current_char+str(count))
		else:
			count += 1

	compressed = "".join(compressed)
	if len(string) < len(compressed):
		return string

	return compressed

print compress("aabcccccaaa") 