import warnings


def register_user(username, age):
    if not username:
        raise ValueError("Имя пользователя не может быть пустым")

    if age < 18:
        raise ValueError("Пользователь должен быть совершеннолетним")

    return {
        "username": username,
        "age": age,
    }


def get_user(users, user_id):
    if user_id not in users:
        raise KeyError(f"Пользователь с id={user_id} не найден")

    return users[user_id]

def clculate_discount(discount):
    if discount > 50:
        warnings.warn(
            "Использована слишком большая скидка",
            UserWarning,
        )
    return discount