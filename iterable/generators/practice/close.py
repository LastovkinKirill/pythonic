def control_gen_lifecycle_outside():
	def count_forever():
		i = 0
		try:
			while True:
				yield i
				i += 1
		except GeneratorExit:
			print("Generator stopped by request")

	gen = count_forever()
	next(gen)
	next(gen)
	gen.close()


def resource_clean_up():
	def file_reader(filename):
		file = open(filename, 'r')
		try:
			for line in file:
				yield line
		finally:
			file.close()
			print("File closed")

	gen = file_reader('data.txt')
	print(next(gen), end='')
	print(next(gen), end='')
	gen.close()
	
def close_internally():
	def some_gen_func():
		yield 1
		yield 2

	def the_same_some_gen_func():
		try:
			yield 1
			yield 2
		except GeneratorExit:
			print("Generator stopped by request")

	gen = some_gen_func()
	print(next(gen))
	gen.close()
	try:
		print(next(gen))
	except StopIteration:
		print("gen closed 1")

	gen = the_same_some_gen_func()
	print(next(gen))
	gen.close()
	try:
		print(next(gen))
	except StopIteration:
		print("gen closed 2")


if __name__ == "__main__":
	control_gen_lifecycle_outside()
	resource_clean_up()
	close_internally()
