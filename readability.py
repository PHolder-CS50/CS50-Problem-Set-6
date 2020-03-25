# Calculate the readability of input text, reporting it as one of
# Less than Grade 1, Grade 1 through 16 or Grade 16+

from cs50 import get_string
import re


# Get input from the user, calculate the readability score, and
# output the grade level
def main():
    input = get_string("Text: ")
    numLetters, numWords, numSentences = computeReadability(input)
    grade = computeColemanLiauIndex(numLetters, numWords, numSentences)
    print(decodeGrade(grade))


# determine the number of letters, words and sentences in an input
# and return them as a tuple
def computeReadability(input):
    sentences = re.findall(r"(?:\s*)(\w[-,'\w\s]*[.?!])", input)
    numLetters = len(re.findall(r"\w", input))
    numWords = len(re.findall(r"[-\w']+", input))
    numSentences = len(sentences)

    # Some commented out debug because regular expressions can be hard
    # to get right
    # print(sentences)
    # print(f"numLetters={numLetters}")
    # print(f"numWords={numWords}")
    # print(f"numSentences={numSentences}")
    return (numLetters, numWords, numSentences)


# Compute readability as a grade using the Coleman-Liau index
def computeColemanLiauIndex(numLetters, numWords, numSentences):
    L = numLetters * 100.0 / numWords
    S = numSentences * 100.0 / numWords
    return int(round(0.0588 * L - 0.296 * S - 15.8))


# Convert the integer numeric grade to a string
def decodeGrade(grade):
    if grade < 1:
        return "Before Grade 1"
    elif grade >= 16:
        return "Grade 16+"
    else:
        return "Grade {}".format(grade)


# Run the program
main()
