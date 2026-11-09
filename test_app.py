import unittest
from unittest.mock import call, patch
import Week2.app_two as app_two


class HelloWorldTests(unittest.TestCase):
    @patch("app_two.random.randint", side_effect=[12, 30])
    def test_hello_world_returns_customer_number(self, randint):
        response = app_two.hello_world()

        self.assertEqual(
            response,
            "<p>Congratulations you are customer number  42 today!</p>",
        )
        self.assertEqual(randint.call_args_list, [call(1, 100), call(1, 100)])


if __name__ == "__main__":
    unittest.main()