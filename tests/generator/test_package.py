import generator


def test_generator_package_exposes_only_public_entrypoints() -> None:
    assert generator.__all__ == ["download_schema", "generate"]
