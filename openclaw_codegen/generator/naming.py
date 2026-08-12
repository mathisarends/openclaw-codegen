import keyword
import re
from typing import Any


def snake_case(value: str) -> str:
    value = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9_]", "_", value).lower()
    if not value or value[0].isdigit():
        value = f"field_{value}"
    return f"{value}_" if keyword.iskeyword(value) else value


def field_name(value: str) -> str:
    name = snake_case(value)
    return f"{name}_" if name == "schema" else name


def client_class_name(domain: str) -> str:
    return f"{pascal_case(domain)}Client"


def pascal_case(value: str) -> str:
    return "".join(part.capitalize() for part in snake_case(value).removesuffix("_").split("_"))


def model_stem(name: str) -> str:
    return name.removesuffix("Params").removesuffix("Result").removesuffix("Ack")


def operation_stem(method: str) -> str:
    return re.sub(r"[^a-z0-9]", "", method.lower())


def normalized_stem(value: str) -> str:
    """Word-wise stem that ignores casing, separators and singular/plural spelling.

    Applied to both sides of a lookup it lets ``sessions.viewers.set`` reach
    ``SessionsViewerSetParams``, which `operation_stem` misses.
    """
    return ".".join(_singular(word.lower()) for word in _WORD_PATTERN.findall(value))


def method_member(method: str) -> str:
    return snake_case(_relative_method(method).replace(".", "_")).upper()


def client_method_name(method: str) -> str:
    parts = _relative_method(method).split(".")
    if len(parts) > 1:
        parts.reverse()
    return "_".join(snake_case(part) for part in parts)


def _relative_method(method: str) -> str:
    return method.split(".", 1)[1] if "." in method else method


_WORD_PATTERN = re.compile(r"[A-Z]+(?![a-z])|[A-Z][a-z0-9]*|[a-z0-9]+")


def _singular(word: str) -> str:
    if word.endswith("ies") and len(word) > 4:
        return f"{word[:-3]}y"
    if word.endswith(("sses", "shes", "ches")):
        return word[:-2]
    if word.endswith("s") and not word.endswith(("ss", "us", "is")) and len(word) > 3:
        return word[:-1]
    return word


def python_literal(value: Any) -> str:
    if value is True:
        return "True"
    if value is False:
        return "False"
    if value is None:
        return "None"
    return repr(value)
