from markbook.cmdline import parse_args


def test_parse_args_on():
    args = parse_args(["on", "DEFAULT_NAME"])
    assert args.command == "on"
    assert args.title == "DEFAULT_NAME"


def test_parse_args_nb():
    args = parse_args(["nb"])
    assert args.command == "nb"
