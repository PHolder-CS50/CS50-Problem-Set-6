from cs50 import get_int


# Produce a pair of Mario pyramids of height supplied by the user
def main():
    height = getHeight(1, 8)
    outputPyramid(height)


# Prompt for a height that is constrained to be 1 through 9
def getHeight(minHeight, maxHeight):
    while True:
        height = get_int("Height: ")
        if (height >= minHeight and height <= maxHeight):
            break
    return height


# Produce left and right pyramids with two spaces between
def outputPyramid(height):
    for i in range(height):
        print(" " * (height - i - 1), end="")
        print("#" * (i + 1), end="")
        print("  ", end="")
        print("#" * (i + 1), end="")
        print()


# Invoke main and run the program
main()
