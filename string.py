# Am I still in school
from itertools import permutations as permute

# Brisanje nepotrebnih karaktera iz stringa


def replace_char(word):

    chars = [",", ".", "!", "?", "_", ";", ":", '"', "'", "&"]
    for character in chars:
        word = word.replace(character, "")
    return word

# Racunanje broja suglasnika i samoglasnika stringa


def is_vowel(word):
    vowel_count = 0
    consonant_count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for character in word:
        if character in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    print("U stringu je ", vowel_count, " samoglasnika")
    print("U stringu je ", consonant_count, " suglasnika")

# Funkcija koja prebrojava velika i mala slova stringa


def upper_lower_count(word):
    upper_count = 0
    lower_count = 0
    for character in word:
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1
    print("Broj velikih slova je : ", upper_count)
    print("Broj malih slova je : ", lower_count)

# Funkcija koja okrece string unazad


def reverse(word):
    return word[::-1]

# Funkcija koja provjerava da li je string palindrom


def is_palindrome(word):
        if word[::1] == word[::-1]:
            return True
        else:
            return False

# Funkcija koja prebrojava karaktere stringa


def count_char(word):
    count = {}
    for char in word:
        count[char] = word.count(char)
    return count

# Bonus zadatak


def bonus_funkcija(words):
    for word in words:
        for permuted in permute(word):
            res = is_palindrome(permuted)

            if res == 1:
                print(word, " - ova rijec ima permutaciju koja je palindrom.")
                break
            else:
                continue

# MAIN funkcija


def main():

    # Unosenje stringa i pravljenje verzije stringa sa svim malim slovima, bez razmaka i interpunkcijskih znakova

    string_input = input("Unesite string: ")
    string_input_lower = string_input.lower()
    string_input_replaced = replace_char(string_input_lower)
    string_input_stripped = string_input_replaced.replace(" ", "")
    reverse(string_input)
    is_palindrome(string_input_stripped)

    answer = is_palindrome(string_input_stripped)
    if answer == 1:
        print("Uneseni string je palindrom.")
    else:
        print("Uneseni string nije palindrom.")

# Rasclanjivanje stringa na rijeci
    string_input_split = string_input_replaced.split(" ")

# Postavljanje default vrijednosti za broj rijeci i duzine rijeci
    word_count = 0
    words_lenght = 0

# Provjeravanje da li je neka rijec iz unesenog stringa palindrom, ako jeste ispisujem je
    for word in string_input_split:
        word_count += 1
        words_lenght += len(word)

        if is_palindrome(word):
            print(word, " - Ova rijec stringa je palindrom")
        else:
            continue

    word_av_lenght = words_lenght/word_count

# Ispisivanje broja samoglasnika i suglasnika
    is_vowel(string_input_stripped)

# Ispisivanje koliko puta se koji simbol pojavljuje u stringu
    print(count_char(string_input_lower))

# Ispisivanje duzine stringa
    print("Duzina stringa: ", len(string_input))

# Ispisivanje broja rijeci
    print("Broj rijeci je: ", word_count)

# Ispisivanje prosjecne duzine rijeci
    print("Prosjecna duzina rijeci je: ", word_av_lenght)

# Ispisivanje broja velikih i malih slova
    upper_lower_count(string_input)

# Ispisivanje unesenog stringa unazad
    print("Uneseni string unazad: ", reverse(string_input))

# Ispisivanje bonus zadatka
    print("___________________________________________________________________________________")
    print("Bonus zadatak")
    bonus_funkcija(string_input_split)


main()
