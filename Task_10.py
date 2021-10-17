def most_common_letters(word1, word2):
    """This function returns the letters that are common to the
    two strings passed into it."""
    word1 = set(word1.lower()[0:])
    word2 = set(word2.lower()[0:])
    common_letters = word1.intersection(word2)
    return "Common letters: " + ", ".join(common_letters)

print(most_common_letters("testing", "coding"))
    
