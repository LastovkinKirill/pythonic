from typing import Optional


class MyContext:
	def __enter__(self) -> Optional['MyContext']:
		print("Enter")
		return self

	def __exit__(self, exc_type, exc_value, traceback) -> Optional[bool]:
		print("Exit", exc_type, exc_value, traceback)


def equivalent(error: bool):
	manager = MyContext()
	value = manager.__enter__()
	try:
		print("Inside", value)
		if error:
			raise Exception
	except Exception as exc:
		suppress = manager.__exit__(type(exc), exc, exc.__traceback__)
		if not suppress:
			raise
	else:
		manager.__exit__(None, None, None)


def equivalent_exc_not_important():
	manager = MyContext()
	value = manager.__enter__()
	try:
		print("Inside", value)
	finally:
		manager.__exit__(None, None, None)


if __name__ == '__main__':
	with MyContext() as con:
		print(con)

	print('----------------')
	equivalent(error=False)
	print('----------------')
	equivalent(error=True)
	print('----------------')
	equivalent_exc_not_important()
