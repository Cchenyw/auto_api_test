import pytest

test_data = (1, 2)


@pytest.mark.parametrize("items", test_data)
def test_demo(items):
    print(items)


if __name__ == "__main__":
    pytest.main()
