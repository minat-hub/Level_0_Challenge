def vowels_in_strings(strings):
    """This function prints out the vowels in a string."""
    vowels = ["a", "e", "i", "o", "u"]
    counting_vowels = []
    for letter in strings.lower():
        if letter in vowels:
            if letter not in counting_vowels:
                counting_vowels.append(letter)
                total_count = ", ".join(counting_vowels)
    print("Vowels: {}".format(total_count))

vowels_in_strings("umuzi")