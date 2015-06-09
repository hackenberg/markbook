import unittest

from markbook.cmdline import parse_args


class ParseArgsTestCase(unittest.TestCase):

    def test_parse_args_on(self):
        args = parse_args(["on", "DEFAULT_NAME"])
        self.assertEqual(args.command, "on")
        self.assertEqual(args.title, "DEFAULT_NAME")

    def test_parse_args_nb(self):
        args = parse_args(["nb"])
        self.assertEqual(args.command, "nb")


if __name__ == "__main__":
    unittest.main()
