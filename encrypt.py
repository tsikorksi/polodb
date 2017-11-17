"""
Encryption functions
"""


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
        message_int += shift
        x.append(chr(message_int))
    return x


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
