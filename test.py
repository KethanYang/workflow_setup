from main import add

def test_add():
	assert add(11, 11) == 22

if __name__ == "__main__":
	test_add()
	print("All tests passed.")
