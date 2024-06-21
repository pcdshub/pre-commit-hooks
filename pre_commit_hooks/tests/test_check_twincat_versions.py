from importlib.resources import files

import pre_commit_hooks.tests.data as test_data
from pre_commit_hooks.check_twincat_versions import tc_version_pinned


def test_pinned_version():
    tsproj_filename = files(test_data).joinpath("pinned-version-3.1.4024.44.tsproj")
    assert tc_version_pinned(tsproj_filename)


def test_absent_pinned_version():
    tsproj_filename = files(test_data).joinpath("version-3.1.4024.22.tsproj")
    assert not tc_version_pinned(tsproj_filename)
