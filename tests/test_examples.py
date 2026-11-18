"""Exercise public examples without executing the SQLModel database playground."""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import os
import platform
from collections.abc import Iterator
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "sqlmodel-app"


def example_hashes() -> dict[str, str]:
    paths = sorted(EXAMPLES.glob("*.py")) + sorted(EXAMPLES.glob("*.db"))
    return {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}


@pytest.fixture(autouse=True)
def examples_and_databases_remain_unchanged() -> Iterator[None]:
    before = example_hashes()
    yield
    assert example_hashes() == before


def test_actual_python_matches_the_independent_row() -> None:
    expected = os.environ["STUDY_EXPECTED_PYTHON"]
    assert expected in {"3.10", "3.12"}
    assert ".".join(platform.python_version_tuple()[:2]) == expected


def test_all_authored_tutorial_modules_parse_without_execution() -> None:
    sources = sorted(EXAMPLES.glob("*.py"))
    assert {path.name for path in sources} >= {"main.py", "database.py"}
    for source in sources:
        ast.parse(source.read_text(), filename=str(source))


def test_original_root_route_returns_hello_world_in_process() -> None:
    assert os.environ["OTEL_SDK_DISABLED"] == "true"
    spec = importlib.util.spec_from_file_location(
        "public_study_main", EXAMPLES / "main.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with TestClient(module.app) as client:
        response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
