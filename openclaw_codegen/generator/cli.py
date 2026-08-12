"""Command-line entry point for generating the OpenClaw client."""

import argparse

from .pipeline import generate
from .schema_download import download_schema


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--check", action="store_true", help="fail if regeneration would change tracked output")
    action.add_argument(
        "--download-schema",
        metavar="VERSION",
        help="download an explicit published VERSION, update its pin, and regenerate",
    )
    return parser.parse_args()


def main() -> None:
    """Run the generator command-line interface."""
    args = _parse_args()
    if args.download_schema is not None:
        download_schema(version=args.download_schema)
    generate(check=args.check)
