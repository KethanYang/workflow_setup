from main import subtract

def test_subtract():
	assert subtract(22, 11) == 11

if __name__ == "__main__":
	test_subtract()
	print("All tests passed.")
