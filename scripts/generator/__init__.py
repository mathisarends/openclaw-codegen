"""Implementation package for the OpenClaw client generator."""

from .pipeline import generate
from .schema_download import download_schema

__all__ = ["download_schema", "generate"]
