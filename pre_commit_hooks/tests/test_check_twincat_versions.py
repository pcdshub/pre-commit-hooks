from importlib.resources import files

import pytest

import pre_commit_hooks.tests.data as test_data
from pre_commit_hooks.check_twincat_versions import tc_version_pinned


@pytest.fixture
def pinned_4024_44():
    return files(test_data).joinpath("pinned-version-3.1.4024.44.tsproj")

@pytest.fixture
def not_pinned_4024_22():
    return files(test_data).joinpath("version-3.1.4024.22.tsproj")

def test_pinned_version(pinned_4024_44):
    assert tc_version_pinned(pinned_4024_44)


def test_absent_pinned_version(not_pinned_4024_22):
    assert not tc_version_pinned(not_pinned_4024_22)
