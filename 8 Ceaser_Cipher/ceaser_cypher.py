import art


print(art.logo)


def cypher(word, shift_number, cypher_direction):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_word = ""
    if cypher_direction == "decode":
        shift_number *= -1
    for letter in word:
        if letter in alphabets:
            letter_index = alphabets.index(letter)
            new_position = letter_index + shift_number
            encrypted_word += alphabets[new_position]
        else:
            encrypted_word += letter
    print(f'The {cypher_direction}d word is {encrypted_word}')


flag = True
while flag:
    message = input("Please enter your message: ").lower()
    code_number = int(input("Please enter your number (1-26): "))
    encryption = input("Type 'encode to Encode and 'decode' to Decode: ").lower()
    code_number %= 26
    cypher(word=message, shift_number=code_number, cypher_direction=encryption)
    rerun = input("Do you want to encrypt another word? yes or no: ").lower()
    if rerun == 'no':
        flag = False
        print("Goodbye!")
