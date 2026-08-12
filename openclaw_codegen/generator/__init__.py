"""Implementation package for the OpenClaw client generator."""

from openclaw_codegen.generator.cli import main
from openclaw_codegen.generator.pipeline import generate
from openclaw_codegen.generator.schema_download import download_schema

__all__ = ["download_schema", "generate", "main"]
