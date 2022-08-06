from morse_code import morse_code


def morse_generator(text):
    split_text = [morse_code[char.upper()] for char in text]
    return ''.join(split_text)


if __name__ == '__main__':
    print(morse_generator('Hello world'))
