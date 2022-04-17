import unittest
import ddt


# decorator class
@ddt.ddt
class DatDemo(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # decorator func
    @ddt.data(("user1", "psw2"), ("user2", "psw2"))
    @ddt.unpack
    def test_ddt(self, username, password):
        print(username, password)


if __name__ == "__main__":
    unittest.main(verbosity=2)
