import random
from tempfile import TemporaryDirectory


def upload_files(tmpdir):
	is_success = random.choice([True, False])
	return is_success


def do_something_with_all_files_in(tmpdir):
	print(f'do_something_with_all_files_in {tmpdir}')


def usage_built_in():
	with open("file.txt") as f:
		data = f.read()
		print(data)

	with TemporaryDirectory() as tmpdir:
		print('tmpdir name', tmpdir)
		is_success = upload_files(tmpdir)
		if is_success:
			do_something_with_all_files_in(tmpdir)
		else:
			print('Remove tmpdir with all files which was successfully uploaded before error')


if __name__ == '__main__':
	usage_built_in()
