import warnings


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError(
            "Сумма должна быть больше нуля"
        )

    if amount > balance:
        raise ValueError(
            "Недостаточно средств"
        )

    if balance - amount < 100:
        warnings.warn(
            "Баланс становится меньше 100",
            UserWarning,
        )

    return balance - amount


def get_account(accounts, account_id):
    if account_id not in accounts:
        raise KeyError(
            f"Счёт с id={account_id} не найден"
        )

    return accounts[account_id]