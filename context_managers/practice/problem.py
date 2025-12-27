if __name__ == '__main__':
	f = open("file.txt")
	try:
		data = f.read()
	finally:
		f.close()

	with open("file.txt") as f:
		data = f.read()