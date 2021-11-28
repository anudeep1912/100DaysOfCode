# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""This programme will create a invitation with starting_letter replacing the [name] with names in
invited_names file and saves the output to output/ReadyToSend.
"""
# read all the lines into a list called name_list
with open("./Input/Names/invited_names.txt", "r") as name_data:
    name_list = name_data.read().splitlines()

# Run through the name list and and crate a  new letter content with new name and write it to file.
with open("./Input/Letters/starting_letter.txt", "r") as letter_data:
    letter_content = letter_data.read()
    for name in name_list:
        file = open(f"./Output/ReadyToSend/{name}_invite.txt", "w")
        new_letter_content = letter_content.replace("[name]", name)
        file.write(new_letter_content)


