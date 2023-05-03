
MORSE_DICT = {'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-',
            'a': '.-', 'b': '-...',
            'c': '-.-.', 'd': '-..', 'e': '.',
            'f': '..-.', 'g': '--.', 'h': '....',
            'i': '..', 'j': '.---', 'k': '-.-',
            'l': '.-..', 'm': '--', 'n': '-.',
            'o': '---', 'p': '.--.', 'q': '--.-',
            'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--',
            'x': '-..-', 'y': '-.--', 'z': '--..'
            }



originalInput = input('What?\n')
morseInput = ""

for i in range(0, len(originalInput)):
    morseInput += MORSE_DICT.get(originalInput[i])

print(f"Original input : {originalInput}\nMorse input : {morseInput}")
