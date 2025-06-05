def main():
    word = input("(. ! or ? to end): ")
    result = ""

    p = (word != ".")
    exclaim = (word != "!")
    q = (word != ".")

    while p & exclaim & q:
        result += word
        word = input("(. ! or ? to end): ")

        p = (word != ".")
        exclaim = (word != "!")
        q = (word != ".")

    print(result)