spam = ['apples', 'bananas', 'tofu', 'cats']
apple = ['apples']

def comma_space(l):
	if len(l) > 1:
		l[-1] = "and " + l[-1]
	else:
		return l
	return ', '.join(l)

print(comma_space(apple + spam))