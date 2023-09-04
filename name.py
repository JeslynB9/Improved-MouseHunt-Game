def is_valid_length(name: str) -> bool:
    if len(name) >= 1 and len(name) <= 9:
        return True
    else:
        return False
    pass


def is_valid_start(name: str) -> bool:
    if name[0].isalpha():
        return True
    else:
        return False
    pass


def is_one_word(name: str) -> bool:
    if len(name.strip(' ')) > 1 + int(name.find(' ')) == 0:
        return True
    else:
        return False


def is_valid_name(name: str) -> bool:
    if is_valid_length(name) and is_valid_start(name) and is_one_word(name):
        return True
    else:
        return False
