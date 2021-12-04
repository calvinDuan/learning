def msg_format(msg: str):
    formatted_msg = ''
    for i in range(len(msg)):
        if (i+1) % 15 == 0:
            formatted_msg = formatted_msg + msg[i] + '\n'
        else:
            formatted_msg += msg[i]
    return formatted_msg


