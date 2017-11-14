def formatting(arr):
    """
    :param arr:
    :return:
    """
    for i in range(0, len(arr)):
        print(arr[i], end='')
    print("\n")


def shift_encode(message, shift):
    """
    :param message: str
    :param shift: int
    :return x: list
    """
    x = []
    if shift >= 26:
        shift %= 26
    for i in range(0, len(message)):
        message_int = ord(message[i])
        """if message_int + shift > 122:
            message_int = message_int + shift - 26
        else:
            message_int += shift"""
        x.append(chr(message_int))
    return x
    # formatting(x)


def shift_decode(message, shift):
    """
    :param message:
    :param shift:
    :return:
    """
    x = []
    if shift >= 26:
        shift %= 26
    for i in range(0, len(message)):
        message_int = ord(message[i])
        message_int -= shift
        x.append(chr(message_int))
    return x
    # formatting(x)
