#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = []
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_content:
    original_letter = letter_content.read()

target_word = "[name]"

for name in names:
    tmp_letter = original_letter
    name_without_newlines = name.strip()
    new_letter_content = ""

    new_letter_content += tmp_letter.replace(target_word, name_without_newlines)
    new_letter_content += "\n"

    with open(f"./Output/ReadyToSend/{name_without_newlines}_letter.txt", mode="w") as new_letter_file:
        new_letter_file.write(new_letter_content)




