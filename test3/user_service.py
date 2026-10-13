def create_user(name, age):
    return {
        "id": 1,
        "name": name,
        "age": age,
        "active": True,
        "roles": ["user"],
    }


def get_adult_users(users):
    return [
        user
        for user in users
        if user["age"] >= 18
    ]


def has_permission(user, permission):
    return permission in user["permissions"]