def one_away(start,end):
	i = 0
	j = 0
	diff = 0

	if abs(len(start) - len(end)) > 1:
		return False

	while i < len(start):
		while j < len(end):
			if diff > 1:
				return False
			if start[i] != end[j]:
				diff +=1
			i+=1
			j+=1
		i+=1
	return True

print one_away("pale","plel")