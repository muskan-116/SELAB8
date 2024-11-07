import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from unittest.mock import Mock
from login import login  # Import the login function from your module

# def test_login_with_mock():
#     """Test login with a mocked database."""

#     # Create a mock object for the database
#     mock_database = Mock()

#     # Set up the return value of the mock's find_user method
#     mock_database.find_user.return_value = {"username": "user", "password": "password"}

#     # This assertion should fail because the login function does not check the mock database yet
#     assert login("user", "password") == True, "Expected login to succeed for valid credentials"

def test_login_with_mock():
    """Test login with a mocked database."""

    # Create a mock object for the database
    mock_database = Mock()

    # Set up the return value of the mock's find_user method for a valid user
    mock_database.find_user.return_value = {"username": "user", "password": "password"}

    # This assertion should pass because the login function checks the mock database
    assert login("user", "password", mock_database) == True, "Expected login to succeed for valid credentials"

    # Test with incorrect password
    mock_database.find_user.return_value = {"username": "user", "password": "wrong_password"}
    assert login("user", "password", mock_database) == False, "Expected login to fail for invalid password"

    # Test with non-existing user
    mock_database.find_user.return_value = None
    assert login("non_existing_user", "password", mock_database) == False, "Expected login to fail for non-existing user"