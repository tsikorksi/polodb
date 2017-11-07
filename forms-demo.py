test = ["a.a.a.a.a.", "b.b.b.b.b"]
final_array = []


def formatting(arr):
    """
    :param arr:
    :return:
    """
    for i in range(0, len(arr)):
        print(arr[i], end='')
    print("\n")


def split():
    for i in range(0,len(test)):
        temp = test[i]
        return_array = []

        for j in range(0, len(temp)):
            if temp[j] == ".":
                pass
            else:
                return_array.append(temp[j])
        final_array.append(return_array)
    formatting(final_array)


def shift_encode(message, shift):
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
        if message_int + shift > 122:
            message_int = message_int + shift - 26
        else:
            message_int += shift
        x.append(chr(message_int))
    formatting(x)


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
        if message_int - shift < 97:
            message_int += 26
        message_int -= shift
        x.append(chr(message_int))
    formatting(x)

split()


