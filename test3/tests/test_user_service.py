from test3.user_service import create_user, get_adult_users

new_user = create_user('Alex',25)

def test_create_user():
    assert isinstance(new_user,dict)

def test_user_exists():
    assert new_user['id'] == 1

def test_user_username():
    assert new_user['name'] == 'Alex'

def test_user_age():
    assert new_user['age'] == 25

def test_user_active():
    assert new_user['active'] == True

def test_user_roles():
    assert 'user' in new_user['roles']

def test_password_not():
    assert 'password' not in new_user

users = [
    {"name": "Alex", "age": 25},
    {"name": "Anna", "age": 17},
    {"name": "Max", "age": 18},
]

adult_users = get_adult_users(users)
adult_names = [
    user['name']
    for user in adult_users
]
def test_adult():
    assert len(adult_users) == 2
    assert 'Alex' in adult_names
    assert 'Anna' not in adult_names
    assert 'Max' in adult_names