import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from add import add
import pytest
def test_add():
    """Test the add function."""
    assert add(1, 2) == 3, "Expected the sum of 1 and 2 to be 3"
    assert add(-1, 1) == 0, "Expected the sum of -1 and 1 to be 0"
    assert add(0, 0) == 0, "Expected the sum of 0 and 0 to be 0"
