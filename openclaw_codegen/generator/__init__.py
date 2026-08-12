"""Implementation package for the OpenClaw client generator."""

from .cli import main
from .pipeline import generate
from .schema_download import download_schema

__all__ = ["download_schema", "generate", "main"]
