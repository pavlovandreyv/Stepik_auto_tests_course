from multiprocessing import Condition
from pickle import TRUE
import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert TRUE


@pytest.mark.xfail()
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False