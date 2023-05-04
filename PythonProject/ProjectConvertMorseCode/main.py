
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

morseRes = []
stringRes = []
strToMorse = True

while strToMorse:
    print("Choose the number.")
    print("1. String to Morse code.")
    print("2. See what I input so far.")
    print("3. Exit.")
    menu = int(input("-> "))


    if menu == 1:
        originalInput = input('What?\n')
        morseInput = ""

        for i in range(0, len(originalInput)):
            morseInput += MORSE_DICT.get(originalInput[i])

        print(f"Original input : {originalInput}\nMorse input : {morseInput}\n")
        stringRes.append(originalInput)
        morseRes.append(morseInput)
    elif menu == 2:
        print("--- String input ---")
        for i in range(0, len(stringRes)):
            print(stringRes[i])
        print()
        for i in range(0, len(morseRes)):
            print(morseRes[i])
        print("\n")
    elif menu == 3:
        strToMorse = False
    else:
        print("Wrong input.\nPlease input again.\n")

