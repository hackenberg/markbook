#!/usr/bin/env python3
import argparse
import sys
import webbrowser

from server import app, db
import server.util


def init():
    db.create_all()


def parse_args(args):
    parser = argparse.ArgumentParser(description="Description (TODO)")
    subparsers = parser.add_subparsers(help="Help (TODO)", dest="command")

    on_parser = subparsers.add_parser("on")
    nb_parser = subparsers.add_parser("nb")

    parser.add_argument("--init", action="store_true", help="Help (TODO)")
    parser.add_argument("--start-server", dest="start_server",
                        action="store_true", help="Help (TODO)")

    on_parser.add_argument("title", help="Help (TODO)")

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])

    if args.init:
        init()

    if args.start_server:
        app.run()
    elif args.command == "on":
        server.util.open_note(args.title)
    elif args.command == "nb":
        webbrowser.open_new_tab("http://localhost:5000")
        app.run()
    else:
        parse_args(["--help"])


if __name__ == "__main__":
    main()
