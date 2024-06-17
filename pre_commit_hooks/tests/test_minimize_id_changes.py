from importlib.resources import files

import pre_commit_hooks.tests.data as test_data
import pytest
from pre_commit_hooks.minimize_id_changes import (PreCommitException,
                                                  minimize_id_changes_checked)


def test_missing_minimize_id_changes():
    plcproj_filename = files(test_data).joinpath("no-minimize-id-changes.plcproj")

    with pytest.raises(PreCommitException):
        minimize_id_changes_checked(plcproj_filename)


def test_enabled_minimize_id_changes():
    plcproj_filename = files(test_data).joinpath("minimize-id-changes-enabled.plcproj")

    # Doesnt raise PreCommitException
    minimize_id_changes_checked(plcproj_filename)
