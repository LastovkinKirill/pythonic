from typing import Iterable


def get_built_it_iterables():
	lists = [1, 2, 3]
	tuples = (1, 2, 3)
	strings = "hello"
	sets = {1, 2, 3}
	dicts = {'a': 1, 'b': 2}
	range_objects = range(5)

	print(lists, tuples, strings, sets, dicts, range_objects)


def check_iterable(iterable: Iterable):
	print(iterable, isinstance(iterable, Iterable))
	print(iterable, hasattr(iterable, '__iter__'))


class List:
	_list = [1, 2, 3]

	def __iter__(self):
		return iter(self._list)


class ListWithIndexes:
	_list = [1, 2, 3]

	def __getitem__(self, item):
		return self._list[item]


if __name__ == '__main__':
	get_built_it_iterables()

	check_iterable(range(5))
	check_iterable([1, 2])

	check_iterable(enumerate([1, 2]))
	check_iterable(zip([1, 2], [3, 4]))

	map_iterator = map(lambda x: x ** 2, [1, 2, 3])
	check_iterable(map_iterator)

	filter_iterator = filter(lambda x: x % 2 == 0, [1, 2, 3])
	check_iterable(filter_iterator)

	for i in List():
		print(i)

	l = ListWithIndexes()
	print(l[0])
	for i in l:
		print(i)
