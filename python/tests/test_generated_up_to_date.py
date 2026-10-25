"""The generated modules must match spec/endpoints.json (run scripts/generate.py)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_generated_code_is_up_to_date() -> None:
    bindir = Path(sys.executable).parent
    if not ((bindir / "ruff").exists() or (bindir / "ruff.exe").exists()):
        pytest.skip("ruff not installed next to the interpreter")
    result = subprocess.run(
        [sys.executable, "-I", str(ROOT / "scripts" / "generate.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
