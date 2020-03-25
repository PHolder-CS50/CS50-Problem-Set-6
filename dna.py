# DNA matcher  Takes a CSV database and a sequence on the first line of an input
# file, and determines if the sequence matches anyone in the database or else
# it outputs "No match"


import csv
import re
from sys import argv


# Get the database filename as command line argument 1 and the sequence filename
# as command line argument 2
# load the candiates from the database
# load the sequence from the file
# attempt to perform a match and output first match found
def main():
    if not len(argv) == 3:
        print("Usage: python dna.py data.csv sequence.txt")
    else:
        strands, candidates = loadCandidates(argv[1])
        # print(strands)
        # print(candidates)
        sequence = inputSequence(argv[2])
        # print(sequence)
        strandCounts = extractStrandCounts(strands, sequence)
        # print(strandCounts)
        didMatch, match = findMatch(candidates, strandCounts)
        if didMatch:
            print(match)
        else:
            print("No match")


# loads the candidates from the CSV database file given the filename
# Reads the header line to find the strad sequences in the database and
# returns them as the first member of a tuple
# the second member of the tuple is the list of candidates
# in the list of candidates, each candidate is also a list, where
# the first element is the name, and the remaining elements are the
# integer counts of strand lengths
def loadCandidates(filename):
    strands = []
    candidates = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        # read the first line to extract the header line and
        # use the header elements as the strands
        headers = reader.__next__()
        for i in range(len(headers)):
            if i > 0:
                strands.append(headers[i])
        # read the rest of the file after the header line
        for row in reader:
            rowWithInts = []
            for i in range(len(row)):
                if i == 0:
                    rowWithInts.append(row[0])
                else:
                    rowWithInts.append(int(row[i]))
            candidates.append(rowWithInts)
    return strands, candidates


# load the input sequence from the first line of the supplied filename
def inputSequence(filename):
    with open(filename, "r") as f:
        return f.read()


# Finds the longest repeat of each strand in the sequence
def extractStrandCounts(strands, sequence):
    counts = []
    for strand in strands:
        regexpr = "((?:{})+)".format(strand)
        # print(regexpr)
        matches = re.findall(regexpr, sequence)
        # print(matches)
        longestCount = getLongestCount(matches, len(strand))
        # print(longestCount)
        counts.append(longestCount)
    return counts


# because the regular expression can match multiple repeats
# in the sequence, this routine finds the longest of the
# repeats and converts it to a number of repeats
def getLongestCount(matches, strandLength):
    max = 0
    longest = ""
    for match in matches:
        if len(match) > max:
            max = len(match)
            longest = match
    result = int(len(longest) / strandLength)
    # print(f"max={max} longest={longest} result={result}")
    return result


# Look through the candidates to find any possible match
# resturns a tuple, the first element is a boolean indicating
# if any match occured, and the second element is the name of
# the match
def findMatch(candidates, strandCounts):
    # print(f"findMatch: strandCounts={strandCounts}")
    didMatch = False
    matchName = ""
    for candidate in candidates:
        # print(f"candidate={candidate}")
        numMatches = 0
        for i in range(len(candidate)):
            if i == 0:
                potentialMatchName = candidate[i]
            else:
                # print(f"candidate[i]={candidate[i]} strandCounts[i - 1]={strandCounts[i - 1]}")
                if candidate[i] == strandCounts[i - 1]:
                    numMatches += 1
        # print(f"potentialMatchName={potentialMatchName} numMatches={numMatches}")
        if numMatches == len(strandCounts):
            didMatch = True
            matchName = potentialMatchName
            break

    return (didMatch, matchName)


# Run the program
main()
