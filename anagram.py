import time
word = input(str("what is your first word?\n"))
anagram = input(str("what is your second word?\n"))
def find_anagram(word,anagram):
    if sorted(word) == sorted(anagram):
        print("Good!.This is an anagram")
    else:
        print("No!.This is not an anagram")
find_anagram(word,anagram)