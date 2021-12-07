import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
nato_dict = {row["letter"]: row["code"] for (index, row) in nato_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    try:
        word = input("Please enter a word: ")
        print([nato_dict[i.upper()] for i in word])
        break
    except KeyError:
        print("Please enter alphabets only in a single string.")




