import openclaw_codegen
from openclaw_codegen import generator


def test_generator_package_exposes_only_public_entrypoints() -> None:
    assert generator.__all__ == ["download_schema", "generate", "main"]
    assert openclaw_codegen.generate is generator.generate
    assert openclaw_codegen.download_schema is generator.download_schema
