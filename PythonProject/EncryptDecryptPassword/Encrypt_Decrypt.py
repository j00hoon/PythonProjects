from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
  final_text = ""
  
  print(f"You choose {direction}!")
  
  for letter in text:
    # if letter.isalpha():
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift
      elif direction == "decode":
        new_position = position - shift
      final_text += alphabet[new_position]  
    else:
      final_text += letter
    
  print(f"The {direction} text is {final_text}")




print(logo)

while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if shift >= 26:
    shift = len(alphabet) % 26 
  
  caesar(text, shift, direction)
  
  ans = input("Restart? yes or no\n")
  if ans == "no":
    break

