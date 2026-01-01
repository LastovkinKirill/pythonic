def count_up_generator_function(max):
	count = 1
	while count <= max:
		yield count
		count += 1


def get_generator_expression():
	return (x ** 2 for x in range(5))


def simple_gen():
	yield 1
	yield 2
	yield 3


def send_value_to_generator():
	def receiver():
		while True:
			try:
				received = yield 'Kirill'
				print(f"Received: {received}")
			except ValueError as e:
				print(e)



	gen = receiver()
	name = next(gen)
	gen.send(f"Hello, {name}")

	gen.throw(ValueError, "Something went wrong")

	gen.close()


if __name__ == '__main__':
	gen = count_up_generator_function(2)
	print(type(count_up_generator_function))
	print(type(gen))

	print(next(gen))
	print(next(gen))
	try:
		print(next(gen))
	except StopIteration:
		pass

	gen = get_generator_expression()
	print(type(gen))

	print(next(gen))
	print(next(gen))

	print(list(gen))
	try:
		print(next(gen))
	except StopIteration:
		pass

	send_value_to_generator()
