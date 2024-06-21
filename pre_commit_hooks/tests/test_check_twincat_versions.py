from importlib.resources import files

import pre_commit_hooks.tests.data as test_data
import pytest
from pre_commit_hooks.check_twincat_versions import (fix_tc_version,
                                                     get_tc_version,
                                                     tc_version_pinned)


@pytest.fixture
def pinned_4024_44():
    return files(test_data).joinpath("pinned-version-3.1.4024.44.tsproj").read_text()


@pytest.fixture
def not_pinned_4024_22():
    return files(test_data).joinpath("version-3.1.4024.22.tsproj").read_text()


@pytest.fixture
def not_pinned_4024_55():
    return files(test_data).joinpath("version-3.1.4024.55.tsproj").read_text()


def test_pinned_version(pinned_4024_44):
    assert tc_version_pinned(pinned_4024_44)


def test_absent_pinned_version(not_pinned_4024_22):
    assert not tc_version_pinned(not_pinned_4024_22)


def test_get_tc_version(pinned_4024_44, not_pinned_4024_22, not_pinned_4024_55):
    assert get_tc_version(pinned_4024_44) == "3.1.4024.44"
    assert get_tc_version(not_pinned_4024_22) == "3.1.4024.22"
    assert get_tc_version(not_pinned_4024_55) == "3.1.4024.55"


def test_fix_tc_version(pinned_4024_44, not_pinned_4024_22):
    changed_version1 = fix_tc_version(pinned_4024_44, "3.1.4024.55")
    assert get_tc_version(changed_version1) == "3.1.4024.55"

    changed_version2 = fix_tc_version(not_pinned_4024_22, "3.1.4024.55")
    assert get_tc_version(changed_version2) == "3.1.4024.55"
