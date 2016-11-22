
def urlify(url):

	url_list = url.split(' ')
	end_url = ""
	for i in range(len(url_list)):
		if i == len(url_list) - 1:
			end_url += url_list[i]
		else:
			end_url += url_list[i] + "%20"

	return end_url

print urlify("Mr John Smith")