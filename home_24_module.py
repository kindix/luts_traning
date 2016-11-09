def count_chars(test_file):
	test_file.seek(0)
	return len(test_file.read())
	
def count_lines(test_file):
	test_file.seek(0)
	return len(test_file.readlines())

def test():
	with open('C:\python34\luts\part20\\test.txt') as test_file:
		return count_lines(test_file), count_chars(test_file)

print(test())