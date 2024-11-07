# def login(username: str, password: str) -> bool:
#     """Dummy login function that does not yet use the database."""
#     return False  # This will lead to the test failing, as it doesn't check against any user.
# src/login.py

def login(username: str, password: str, database) -> bool:
    """Login function that checks credentials against a mocked database."""
    user = database.find_user(username)  # Retrieve the user from the mock database
    if user is None or user["password"] != password:
        return False  # Explicitly return False if user is not found or password doesn't match
    return True  # Return True if credentials are valid

def login(username: str, password: str, database) -> bool:
    """Login function that checks credentials against a mocked database."""
    
    # Attempt to find the user in the database
    user = database.find_user(username)
    
    # Check if the user was found and if the password matches
    if user is None:
        return False  # No such user found
    
    if user["password"] != password:
        return False  # Password does not match
    
    return True  # User found and password matches

