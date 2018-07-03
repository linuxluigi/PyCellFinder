import pytest
import pycellfinder


def test_project_defines_author_and_version():
    assert hasattr(pycellfinder, '__author__')
    assert hasattr(pycellfinder, '__version__')
