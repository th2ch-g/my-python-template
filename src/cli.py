import argparse
import sys

from .logger import generate_logger

LOGGER = generate_logger(__name__)


def cli() -> None:
    # make parser
    parser = argparse.ArgumentParser(description=("Input description here"))

    # subcommands
    # subparsers = parser.add_subparsers()

    # add options
    # parser.add_argument("--option", type=str, default="default", help="Option description")

    _args = parser.parse_args()

    # prohibit no args
    # if len(sys.argv) == 1:
    #     LOGGER.error(f"use {sys.argv[0]} --help")
    #     sys.exit(1)

    # log info
    # LOGGER.info(f"{sys.argv[1]} called")
    # LOGGER.info(f"{sys.argv[1]} finished")
