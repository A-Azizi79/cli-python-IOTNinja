msg_invalid_parameter = "You passed invalid parameter"


def is_valid_param(_class_, obj):
    if isinstance(obj, _class_):
        return True
    else:
        raise Exception(msg_invalid_parameter)
