import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter = data["letter"].tolist()
code = data["code"].tolist()
npa = {letter[i]: code[i] for i in range(len(letter))}
error = True
while error:
    try:
        user_input = input("Type a word or name ").upper()
        output = [npa[letter] for letter in user_input]
    except KeyError:
        print("Only letters from the alphabet")
    else:
        print(output)
        error = False


