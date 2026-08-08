"""Generate the typed OpenClaw protocol client from the pinned JSON schema."""

import argparse

from generator import download_schema, generate


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


def _main() -> None:
    args = _parse_args()
    if args.download_schema is not None:
        download_schema(version=args.download_schema)
    generate(check=args.check)


if __name__ == "__main__":
    _main()
