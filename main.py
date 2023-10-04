"""
Purpose: This program takes keyboard inputs from the user and compile them into morse code.
Tools:
"""

# Make the dictionary of morse code
morse_roles = {
    "Q": "––•–",
    "W": "•––",
    "E": "•",
    "R": "•–•",
    "T": "–",
    "Y": "–•––",
    "U": "••–",
    "I": "••",
    "O": "–––",
    "P": "•––•",
    "A": "•–",
    "S": "•••",
    "D": "–••",
    "F": "••–•",
    "G": "––•",
    "H": "••••",
    "J": "•–––",
    "K": "–•–",
    "L": "•–••",
    "Z": "––••",
    "X": "–••–",
    "C": "–•–•",
    "V": "•••–",
    "B": "–•••",
    "N": "–•",
    "M": "––",
    "1": "•----",
    "2": "••---",
    "3": "•••--",
    "4": "••••-",
    "5": "•••••",
    "6": "-••••",
    "7": "--•••",
    "8": "---••",
    "9": "----•",
    "0": "-----",
    " ": "/",
}

# Make the loop
loop = True
while loop:
    word = input("Morse Code Converter!\nType text to convert to morse code (STOP to stop): ")
    if word == "STOP" or word == "stop":
        loop = False
    else:
        for letter in word:
            print(morse_roles[letter.upper()], end=" ")
        print()
