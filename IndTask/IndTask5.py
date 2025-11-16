class CustomError(Exception):
    pass


def trigger_custom_error(condition):
    if condition:
        raise CustomError("Сработало пользовательское исключение!")
    return "Ошибки нет"