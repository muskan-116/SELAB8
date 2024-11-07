import pytest
#failed data
def test_login_success():
    """Test successful login."""
    assert login("valid_user", "valid_password") is True, "Expected login to succeed for valid credentials"

def test_login_failure():
    """Test failed login with invalid credentials."""
    assert login("invalid_user", "invalid_password") is False, "Expected login to fail for invalid credentials"

def test_login_empty_credentials():
    """Test failed login with empty credentials."""
    assert login("", "") is False, "Expected login to fail for empty username and password"

# Implement the login function
def login(username: str, password: str) -> bool:
    """Simple login function."""
    valid_credentials = {
        "valid_user": "valid_password"  # Add valid credentials here
    }
    return valid_credentials.get(username) == password

def test_login_success():
    """Test successful login."""
    assert login("valid_user", "valid_password") is True, "Expected login to succeed for valid credentials"

def test_login_failure():
    """Test failed login with invalid credentials."""
    assert login("invalid_user", "invalid_password") is False, "Expected login to fail for invalid credentials"

def test_login_empty_credentials():
    """Test failed login with empty credentials."""
    assert login("", "") is False, "Expected login to fail for empty username and password"

# Define valid credentials outside of the function for flexibility
valid_credentials = {
    "valid_user": "valid_password",
    "another_user": "another_password"  # Add more valid users as needed
}

def login(username: str, password: str, credentials: dict = valid_credentials) -> bool:
    """Flexible login function using a credentials dictionary."""
    return credentials.get(username) == password

def test_login_success():
    """Test successful login."""
    assert login("valid_user", "valid_password") is True, "Expected login to succeed for valid credentials"

def test_login_failure():
    """Test failed login with invalid credentials."""
    assert login("invalid_user", "invalid_password") is False, "Expected login to fail for invalid credentials"

def test_login_empty_credentials():
    """Test failed login with empty credentials."""
    assert login("", "") is False, "Expected login to fail for empty username and password"
