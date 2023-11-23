from unittest import TestCase, main
from unittest.mock import patch


def myfunc():
    return "myfunc!!"


class TestMyFunc(TestCase):
    @patch("__main__.myfunc", return_value="mocked!!")
    def test_my_func(self, mock_func):
        self.assertEqual(myfunc(), "mocked!!")
        self.assertIs(myfunc, mock_func)
        mock_func.assert_called_once_with()


if __name__ == "__main__":
    main()
