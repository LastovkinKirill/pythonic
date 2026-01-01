from typing import Iterable


def get_iterator(iterable: Iterable):
	iterator = iter(iterable)
	print(type(iterable), type(iterator))

	print(next(iterator))
	print(next(iterator))
	try:
		print(next(iterator))
	except StopIteration:
		pass


class CountDown:
	def __init__(self, start):
		self.current = start

	def __iter__(self):
		return self

	def __next__(self):
		if self.current <= 0:
			raise StopIteration
		value = self.current
		self.current -= 1
		return value


if __name__ == '__main__':
	get_iterator([1, 2])
	get_iterator(CountDown(3))

	