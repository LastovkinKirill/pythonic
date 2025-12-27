from contextlib import contextmanager


@contextmanager
def cm():
	print("Enter")
	yield "value"
	print("Exit")


@contextmanager
def cm_with_exc():
	print("enter")
	try:
		yield
	finally:
		print("exit")


if __name__ == '__main__':
	with cm() as v:
		print(v)
		print("Inside")
		# raise Exception

	print('-----------')

	with cm_with_exc() as v:
		print(v)
		print("Inside")
		raise Exception
